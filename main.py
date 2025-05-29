import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

# Path to folder containing student images
path = 'student_images'
images = []
classNames = []

# List all files in the image directory
try:
    mylist = os.listdir(path)
except FileNotFoundError:
    print(f"Error: Folder '{path}' not found.")
    exit()

# Load each image and extract the student name
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    if curImg is not None:
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    else:
        print(f"Warning: Couldn't read image {cl}")

# Function to encode all known student faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            encodeList.append(encodings[0])
        else:
            print("Warning: No face found in an image.")
    return encodeList

# Encode all known student images
print("[INFO] Encoding student faces...")
encoded_face_train = findEncodings(images)
print("[INFO] Encoding completed.")

# Function to mark attendance in CSV
def markAttendance(name):
    with open('Attendance.csv', 'a+') as f:
        f.seek(0)
        data = f.readlines()
        nameList = [line.split(',')[0] for line in data]

        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S %p')
            date = now.strftime('%d-%B-%Y')
            f.write(f'\n{name}, {time}, {date}')
            print(f"[MARKED] {name} at {time} on {date}")

# Start webcam
cap = cv2.VideoCapture(0)
print("[INFO] Starting webcam. Press 'q' to quit.")

while True:
    success, img = cap.read()
    if not success:
        print("Error: Couldn't access webcam.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = classNames[matchIndex].capitalize()
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            markAttendance(name)

    cv2.imshow('Webcam - Press q to Exit', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("[INFO] Attendance session ended.")

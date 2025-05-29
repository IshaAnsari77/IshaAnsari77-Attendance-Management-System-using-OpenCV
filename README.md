# Attendance-Management-System-using-OpenCV
This repository contains the code and the steps for the implementation of attendance management system using open CV.

## Project Description

The Attendance Management System is a Python-based application that uses OpenCV for face recognition to record attendance. This project simplifies the attendance tracking process by automating the task using facial recognition technology.

# 📸 Attendance Management System using OpenCV

This project is a **Face Recognition Attendance System** using **Python**, **OpenCV**, and **Streamlit**.  
It uses your webcam to detect faces and mark attendance automatically.

---

## ✨ Features

- Detects faces in real-time using a webcam  
- Matches with stored student images  
- Marks attendance only once per person  
- Saves attendance in a CSV file  
- Shows live video and name with green box  
- Optional web app with Streamlit

---

## 🔧 Tools & Libraries Used

- Python  
- OpenCV  
- face_recognition  
- NumPy  
- Pandas  
- Streamlit


## 🧠 How it Works

1. First, it reads all student images from the `student_images` folder.  
2. Then it opens your webcam and starts scanning faces.  
3. When it finds a face, it checks if it matches a student image.  
4. If it matches, it shows the name on screen and saves the time and date in `Attendance.csv`.  
5. It only saves one entry per person (no repeats).  

---

## 🚀 How to Run

### Step 1: Clone this Project

git clone https://github.com/IshaAnsari77/IshaAnsari77-Attendance-Management-System-using-OpenCV.git
cd IshaAnsari77-Attendance-Management-System-using-OpenCV
-Step 2: Install Required Libraries

pip install opencv-python face_recognition numpy pandas streamlit

-Step 3: Add Student Images
Put your images in the student_images folder.
Name the image file as the student’s name (e.g. isha.jpg).

-Step 4: Run the Project
For normal OpenCV app:

python main.py
For Streamlit web version:

streamlit run app.py
![image](https://github.com/user-attachments/assets/388263ad-cc03-43cb-9950-e3c63bb7dfb9)
![image](https://github.com/user-attachments/assets/3c42dae3-7451-4e85-a137-e0969a588ac6)


📷 Screenshot
Here’s how it looks while running:


✅ It shows a green box on the face
✅ It displays the student name
✅ Attendance gets saved instantly

📄 Attendance Output File
The data is saved in Attendance.csv like this:

Name	Time	Date
Isha ansari	07:48 PM	29-05-2025

📘 License
This project uses the MIT License.

🙌 Created by Isha Ansari
This project is for learning. You can improve it by adding more features. 😊




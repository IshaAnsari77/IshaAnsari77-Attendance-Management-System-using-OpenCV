import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page setup
st.set_page_config(page_title="Attendance System", layout="centered")
st.title("📸 Attendance Management System")
st.subheader("BCA - Rayat Bahra University")

# Show current time
now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
st.caption(f"🕒 Current Time: {now}")

# Initialize session state
if 'show_data' not in st.session_state:
    st.session_state['show_data'] = False

# Button to view attendance
if st.button("📄 View Attendance Sheet"):
    st.session_state['show_data'] = True

# Load data if flag is set
if st.session_state['show_data']:
    if os.path.exists("Attendance.csv"):
        try:
            df = pd.read_csv("Attendance.csv")
            if "Name" not in df.columns:
                # If no headers exist, add them
                df = pd.read_csv("Attendance.csv", names=["Name", "Time", "Date", "Subject"], header=None)

            # Filter by date
            if "Date" in df.columns:
                unique_dates = sorted(df["Date"].unique(), reverse=True)
                selected_date = st.selectbox("📅 Filter by Date", options=["All"] + unique_dates)

                if selected_date != "All":
                    filtered_df = df[df["Date"] == selected_date]
                    st.write(f"Showing attendance for: **{selected_date}** ({len(filtered_df)} records)")
                    st.success(f"👥 Unique Students Marked: {filtered_df['Name'].nunique()}")
                    st.dataframe(filtered_df)
                else:
                    st.success(f"👥 Unique Students Marked: {df['Name'].nunique()}")
                    st.dataframe(df)
            else:
                st.dataframe(df)

            # Download button
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="⬇️ Download Attendance as CSV",
                data=csv,
                file_name='Attendance.csv',
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.warning("⚠️ 'Attendance.csv' not found. Please run attendance first.")

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

# View attendance sheet
if st.button("📄 View Attendance Sheet"):
    if os.path.exists("Attendance.csv"):
        try:
            df = pd.read_csv("Attendance.csv")
            if "Name" not in df.columns:
                # Assume no header in CSV, manually assign columns
                df = pd.read_csv("Attendance.csv", names=["Name", "Time", "Date", "Subject"], header=None)

            # Unique students
            st.success(f"👥 Unique Students Marked: {df['Name'].nunique()}")

            # Filter by date
            if "Date" in df.columns:
                unique_dates = sorted(df["Date"].unique(), reverse=True)
                selected_date = st.selectbox("📅 Filter by Date", options=["All"] + unique_dates)

                if selected_date != "All":
                    filtered_df = df[df["Date"] == selected_date]
                    st.write(f"Showing attendance for: **{selected_date}** ({len(filtered_df)} records)")
                    st.dataframe(filtered_df)
                else:
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

import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="📋 Attendance Dashboard", layout="wide")

# Header
st.markdown("""
    <h2 style='text-align: center; color: #088178;'>📸 Attendance Management System</h2>
    <h4 style='text-align: center; color: grey;'>BCA - Rayat Bahra University</h4>
""", unsafe_allow_html=True)

# Show current time
now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
st.markdown(f"<p style='text-align: center;'>🕒 Current Time: <b>{now}</b></p>", unsafe_allow_html=True)

# Tabs for clean layout
tab1, tab2 = st.tabs(["📄 View Attendance", "⬇️ Download CSV"])

# Load and read data
if os.path.exists("Attendance.csv"):
    df = pd.read_csv("Attendance.csv", on_bad_lines='skip', header=None)

    if df.shape[1] == 3:
        df.columns = ["Name", "Time", "Date"]
    elif df.shape[1] == 4:
        df.columns = ["Name", "Time", "Date", "Subject"]
    else:
        st.error("⚠️ Unexpected number of columns in Attendance.csv.")
        st.stop()

    # Tab 1 – View
    with tab1:
        st.subheader("🔍 Filter & Explore Attendance")
        unique_dates = sorted(df["Date"].unique(), reverse=True)
        selected_date = st.selectbox("📅 Select Date", options=["All"] + unique_dates)

        if selected_date != "All":
            filtered_df = df[df["Date"] == selected_date]
            st.success(f"✅ Records found: {len(filtered_df)} | Unique Students: {filtered_df['Name'].nunique()}")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.success(f"✅ Total records: {len(df)} | Unique Students: {df['Name'].nunique()}")
            st.dataframe(df, use_container_width=True)

    # Tab 2 – Download
    with tab2:
        st.subheader("📁 Download Attendance Sheet")
        st.markdown("Click below to download the attendance data as a CSV file:")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Attendance CSV",
            data=csv,
            file_name="Attendance.csv",
            mime="text/csv",
            use_container_width=True
        )
else:
    st.warning("⚠️ Attendance.csv not found. Please run the attendance script first.")

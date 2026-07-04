# 📷 QR Code Attendance System

A Python-based QR Code Attendance System that generates unique QR codes for students and records attendance by scanning QR codes.

## Features

- Generate unique QR code for each student
- Store student details
- Scan QR code using webcam
- Mark attendance automatically
- Prevent duplicate attendance
- Save attendance records in CSV format

---

## Technologies Used

- Python
- OpenCV
- QRCode
- Pandas
- Pillow

---

## Project Structure

```
QR_Attendance_System/
│
├── generate_qr.py
├── scan_attendance.py
├── attendance.csv
├── students.csv
├── requirements.txt
├── README.md
├── qr_codes/
└──output qr screenshots/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/QR_Attendance_System.git
```

Move into the project directory

```bash
cd QR_Attendance_System
```

Install required packages

```bash
pip install -r requirements.txt
```

Run QR Code Generator

```bash
python generate_qr.py
```

Run Attendance Scanner

```bash
python scan_attendance.py
```

---

## How It Works

1. Enter student name and roll number.
2. Generate a unique QR code.
3. QR code is saved in the `qr_codes` folder.
4. Scan the QR code using the webcam.
5. Attendance is recorded automatically in `attendance.csv`.

---

## Output Files

### students.csv

Stores student information.

### attendance.csv

Stores attendance with:

- Student Name
- Roll Number
- Date
- Time
- Status

---

## Future Improvements

- Streamlit Web Interface
- Face Recognition
- Database Integration
- Email Notifications
- Attendance Dashboard
- Export to Excel

---

## Author

Lakshmi Sree 
import cv2
import csv
from datetime import datetime


file = "attendance.csv"


def mark_attendance(data):

    now = datetime.now()

    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    details = data.split(",")

    name = details[0].split(":")[1]
    roll = details[1].split(":")[1]


    with open(file, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            [name, roll, date, time]
        )


    print("Attendance Marked Successfully!")
    print("Name:", name)
    print("Roll No:", roll)



# Open camera

camera = cv2.VideoCapture(0)

qr_detector = cv2.QRCodeDetector()


while True:

    ret, frame = camera.read()


    data, points, _ = qr_detector.detectAndDecode(frame)


    if data:

        print("QR Detected:", data)

        mark_attendance(data)

        break


    cv2.imshow("QR Scanner", frame)


    if cv2.waitKey(1) == ord("q"):
        break



camera.release()
cv2.destroyAllWindows()
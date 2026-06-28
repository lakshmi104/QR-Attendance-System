import qrcode
import csv
import os


number = int(input("Enter number of students: "))


for i in range(number):

    print("\nStudent", i+1)

    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")


    data = f"Name:{name},Roll:{roll}"


    # Save student details

    with open("students.csv","a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [name, roll]
        )


    # Generate QR

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )


    qr.add_data(data)

    qr.make(fit=True)


    img = qr.make_image()


    filename = roll + ".png"

    img.save(filename)


    print("QR Generated:", filename)



print("\nAll Students Registered Successfully!")
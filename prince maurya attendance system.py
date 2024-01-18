#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Prince Maurya
#
# Created:     22-12-2023
# Copyright:   (c) Prince Maurya 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import cv2
import qrcode
import datetime

class StudentException(Exception):
    print("System error found")

class Student:
    def __init__(self):
        self.accounts = []
        self.student_data = self.load_student_data("C:\\Users\\Prince Maurya\\Desktop\\student_datas.txt")

    def load_student_data(self, file_path):
        student_data = {}
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    roll_number, name, class_name, division = line.strip().split(',')
                    student_data[roll_number] = {'name': name, 'class': class_name, 'division': division}
                except ValueError:
                    print(f"Error in line {line_number}: {line}")
        return student_data

    def mainpage(self):
        option = {
            1: self.admin
        }

        print("|------------Student Attendance-----------|")
        print("|press 1. Login                           |")
        print("|press 2. Exit                            |")
        print("|-----------------------------------------|")

        choice = int(input("press 1/2: "))

        if choice in option:
            option[choice]()
        else:
            print("! Invalid option !")

    def admin(self):
        ID = int(input("Login ID: "))
        password = input("Password: ")

        if ID == 1001:
            if password == "prince":
                self.studentdetail()
            else:
                print("! Incorrect Password !")
                self.mainpage()
        else:
            print("! Incorrect Login ID !")
            self.mainpage()

    def studentdetail(self):
        option1 = {
            1: self.student_attendance,
            2: self.search_student,
            3: self.goback
        }
        self.accounts = []
        while True:
            print("|---------ADMIN LOGIN---------|")
            print("|press 1. Student Attendance  |")
            print("|press 2. Search Student      |")
            print("|press 3. Go Back             |")
            print("|-----------------------------|")

            choice1 = int(input("press any 1 - 3 : "))

            if choice1 in option1:
                if choice1 == 3:
                    break
                option1[choice1]()
            else:
                print("Invalid choice!")

    def student_attendance(self):
        print("|--------Digital Student Attendance--------|")
        print("|Please place your Student QR code         |")

        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow('QR Code Scanner', frame)

            detector = cv2.QRCodeDetector()
            value, pts, qr_code = detector.detectAndDecode(frame)

            if value:
                roll_number = value
                if roll_number in self.student_data:
                    student_name = self.student_data[roll_number]['name']
                    class_name = self.student_data[roll_number]['class']
                    division = self.student_data[roll_number]['division']
                    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                    attendance_record = f"{roll_number},{student_name},{class_name},{division},{current_date}\n"

                    print("| Present                                                          |")
                    print("| Roll_Number Name \t\t\t Class \t\t Year    \t\t Date      |")
                    print(f"| {roll_number}\t\t\t { student_name}  { class_name} \t\t\t {division} \t\t\t {current_date}|")
                    if not self.check_attendance_record(roll_number, current_date):
                        with open("C:\\Users\\Prince Maurya\\Desktop\\attendancelist.txt", "a") as file:
                            file.write(attendance_record)
                    else:
                        print("| Student already marked present today.                     |")

                else:
                    print(f"Invalid student, Roll Number: {roll_number}")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def check_attendance_record(self, roll_number, current_date):
        with open("C:\\Users\\Prince Maurya\\Desktop\\attendancelist.txt", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if data[0] == roll_number and data[-1] == current_date:
                    return True
        return False

    def search_student(self):
        roll_number = input("Enter the Roll Number to search: ")

        with open("C:\\Users\\Prince Maurya\\Desktop\\attendancelist.txt", "r") as file:
            found = False
            for line in file:
                data = line.strip().split(',')
                if data[0] == roll_number:
                    found = True
                    student_name = data[1]
                    class_name = data[2]
                    division = data[3]
                    date = data[4]
                    print("| Student Attendance Details |")
                    print("| Roll_Number Name \t\t\t Class \t\t Year    \t\t Date      |")
                    print(f"| {roll_number} \t\t\t {student_name} \t {class_name} \t\t\t {division} \t\t\t {date}|")

            if not found:
                print(f"No attendance record found for Roll Number: {roll_number} or students is asbent")


    def goback(self):
        self.mainpage()

if __name__ == "__main__":
    object1 = Student()
    object1.mainpage()

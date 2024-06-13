import argparse
from datetime import datetime
from models.base import Session, engine, Base
from models.hostel import Hostel
from models.room import Room
from models.student import Student
from models.booking import Booking

def create_hostel():
    name = input("Enter hostel name: ")
    address = input("Enter hostel address: ")
    hostel = Hostel.create(session, name, address)
    print(f"Hostel created: {hostel}")

def delete_hostel():
    hostel_id = int(input("Enter hostel ID to delete: "))
    if Hostel.delete(session, hostel_id):
        print("Hostel deleted.")
    else:
        print("Hostel not found.")

def display_hostels():
    hostels = Hostel.get_all(session)
    for hostel in hostels:
        print(hostel)

def find_hostel_by_id():
    hostel_id = int(input("Enter hostel ID to find: "))
    hostel = Hostel.find_by_id(session, hostel_id)
    if hostel:
        print(hostel)
    else:
        print("Hostel not found.")

def create_room():
    hostel_id = int(input("Enter hostel ID: "))
    room_number = input("Enter room number: ")
    capacity = int(input("Enter room capacity: "))
    room = Room.create(session, hostel_id, room_number, capacity)
    print(f"Room created: {room}")

def delete_room():
    room_id = int(input("Enter room ID to delete: "))
    if Room.delete(session, room_id):
        print("Room deleted.")
    else:
        print("Room not found.")

def display_rooms():
    rooms = Room.get_all(session)
    for room in rooms:
        print(room)

def find_room_by_id():
    room_id = int(input("Enter room ID to find: "))
    room = Room.find_by_id(session, room_id)
    if room:
        print(room)
    else:
        print("Room not found.")

def create_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    gender = input("Enter student gender: ")
    student = Student.create(session, name, age, gender)
    print(f"Student created: {student}")

def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    if Student.delete(session, student_id):
        print("Student deleted.")
    else:
        print("Student not found.")

def display_students():
    students = Student.get_all(session)
    for student in students:
        print(student)

def find_student_by_id():
    student_id = int(input("Enter student ID to find: "))
    student = Student.find_by_id(session, student_id)
    if student:
        print(student)
    else:
        print("Student not found.")

def create_booking():
    student_id = int(input("Enter student ID: "))
    room_id = int(input("Enter room ID: "))
    start_date = datetime.strptime(input("Enter start date (YYYY-MM-DD): "), '%Y-%m-%d')
    end_date = datetime.strptime(input("Enter end date (YYYY-MM-DD): "), '%Y-%m-%d')
    booking = Booking.create(session, student_id, room_id, start_date, end_date)
    print(f"Booking created: {booking}")

def delete_booking():
    booking_id = int(input("Enter booking ID to delete: "))
    if Booking.delete(session, booking_id):
        print("Booking deleted.")
    else:
        print("Booking not found.")

def display_bookings():
    bookings = Booking.get_all(session)
    for booking in bookings:
        print(booking)

def find_booking_by_id():
    booking_id = int(input("Enter booking ID to find: "))
    booking = Booking.find_by_id(session, booking_id)
    if booking:
        print(booking)
    else:
        print("Booking not found.")

def main_menu():
    while True:
        print("\nHostel Management System")
        print("1. Manage Hostels")
        print("2. Manage Rooms")
        print("3. Manage Students")
        print("4. Manage Bookings")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_hostels()
        elif choice == '2':
            manage_rooms()
        elif choice == '3':
            manage_students()
        elif choice == '4':
            manage_bookings()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_hostels():
    while True:
        print("\nManage Hostels")
        print("1. Create Hostel")
        print("2. Delete Hostel")
        print("3. Display All Hostels")
        print("4. Find Hostel by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_hostel()
        elif choice == '2':
            delete_hostel()
        elif choice == '3':
            display_hostels()
        elif choice == '4':
            find_hostel_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_rooms():
    while True:
        print("\nManage Rooms")
        print("1. Create Room")
        print("2. Delete Room")
        print("3. Display All Rooms")
        print("4. Find Room by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_room()
        elif choice == '2':
            delete_room()
        elif choice == '3':
            display_rooms()
        elif choice == '4':
            find_room_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_students():
    while True:
        print("\nManage Students")
        print("1. Create Student")
        print("2. Delete Student")
        print("3. Display All Students")
        print("4. Find Student by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            display_students()
        elif choice == '4':
            find_student_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_bookings():
    while True:
        print("\nManage Bookings")
        print("1. Create Booking")
        print("2. Delete Booking")
        print("3. Display All Bookings")
        print("4. Find Booking by ID")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            create_booking()
        elif choice == '2':
            delete_booking()
        elif choice == '3':
            display_bookings()
        elif choice == '4':
            find_booking_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    main_menu()

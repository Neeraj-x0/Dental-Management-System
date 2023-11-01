import mysql.connector as sql
from time import gmtime, strftime
import os
import sys

def login(conn):
    print("Hospital Management System")
    print("1. Login")
    print("2. Exit")
    print()
    option = int(input("Enter your choice: "))

    if option == 1:
        user = input('User Name: ')
        user = user.upper()
        cur = conn.cursor()
        cur.execute(
            "select * from accounts where User_Name like '" + user + "'")
        ispresent = 0
        datas = cur.fetchall()

        for i in datas:
            value_1 = i[0]
            value_2 = i[1]

            if user == value_1:
                ispresent = 1
                password = input('Password: ')
                password = password.upper()
                if password == value_2:
                    print()
                    print('Login successful')
                    print()
                    a = strftime("%d %b %Y", gmtime())
                    c = strftime("%a ", gmtime())
                    b = strftime("%H %M %S", gmtime())
                    print('Date:', a)
                    print('Day:', c)
                    print('Time:', b)
                    print()
                    return ispresent
                else:
                    print('Invalid Password')
                    print('Try again')
        if not ispresent:
            return "User not Found"
    elif option == 2:
        os.system('cls')
        sys.exit()


def add_patient_record(conn):
    os.system('cls')
    print()
    print("Patient Details:")
    print()
    name = input('Name: ')
    name = name.upper()
    age = int(input('Age: '))
    doc = input('Doctor Consulted: ')
    doc = doc.upper()
    add = input('Address: ')
    add = add.upper()
    phone_no = int(input('Phone Number: '))
    cur = conn.cursor()
    cur.execute("insert into patient_record values('" + name + "'," +
                str(age) + ",'" + doc + "','" + add + "'," + str(phone_no) + ")")
    conn.commit()
    os.system('cls')
    print('Record added')


def add_salary_record(conn):
    os.system('cls')
    print()
    print("Employee Details:")
    print()
    emp_name = input('Employee Name: ')
    emp_name = emp_name.upper()
    proffession = input('Profession: ')
    proffession = proffession.upper()
    salary = int(input('Salary Amount: '))
    add = input('Address: ')
    add = add.upper()
    phone_no = input('Phone Number: ')
    cur = conn.cursor()
    cur.execute("insert into salary_record values('" +
                emp_name + "','" + proffession + "'," + str(salary) + ",'" + add + "'," + phone_no + ")")
    conn.commit()
    os.system('cls')
    print('Record added')


def view_patient_detail(conn):
    os.system('cls')
    print()
    name = input('Name of the patient: ')
    name = name.upper()
    cur = conn.cursor()
    cur.execute(
        "select * from patient_record where patient_name like '" + str(name) + "'")
    data = cur.fetchall()

    if data:
        for row in data:
            print()
            print("Patient Details:")
            print()
            print('Name:', row[0])
            print('Age:', row[1])
            print('Doctor consulted:', row[2])
            print('Address:', row[3])
            print('Phone Number:', row[4])
            input()
    else:
        print()
        os.system('cls')
        print("Patient Record Does not Exist")


def delete_patient_detail(conn):
    os.system('cls')
    print()
    name = input('Name of the patient: ')
    name = name.upper()
    cur = conn.cursor()
    cur.execute(
        "select * from patient_record where patient_name like '" + str(name) + "'")
    data = cur.fetchall()

    if not data:
        os.system('cls')
        print('No Patient Record found')
    else:
        cur.execute(
            "delete from patient_record where Patient_Name like '" + str(name) + "'")
        os.system('cls')
        print('Record Deleted Successfully')

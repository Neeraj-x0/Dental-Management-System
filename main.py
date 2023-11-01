import mysql.connector as sql
import hospital_functions
import os
os.system('cls')
try:
    conn = sql.connect(host='localhost', user='root',
                       passwd='root', database='hospital_management_system')
    result = hospital_functions.login(conn)
    while True:
        if result == 1:
            print('\t\t\t\t')
            print("1. Add Patients records")
            print("2. Add Salary records")
            print("3. View Patient Detail")
            print("4. Delete patient detail")
            print("5. Exit")
            choice = int(input('Enter an option: '))

            if choice == 1:
                hospital_functions.add_patient_record(conn)
            elif choice == 2:
                hospital_functions.add_salary_record(conn)
            elif choice == 3:
                hospital_functions.view_patient_detail(conn)
            elif choice == 4:
                hospital_functions.delete_patient_detail(conn)
            elif choice == 5:
                os.system('cls')
                break
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print('\n\nSession closed explicitly')
finally:
    if conn.is_connected:
        conn.close()

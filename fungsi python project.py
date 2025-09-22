from operator import truediv

import mysql
from mysql.connector.constants import flag_is_set


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db_digital_diary",
    )
# 1. user management
def register_user(username, fullname, password, date_of_birth, gender):
    db = connect_db()
    cursor = db.cursor()
    sql = "INSERT INTO users (username, fullname, password, date_of_birth, gender) VALUES (%s, %s, %s, %s, %s)"
    val = (username, fullname, password, date_of_birth, gender)
    cursor.execute(sql, val)
    db.commit()
    user_id = cursor.lastrowid
    print("Login successful, Welcome {fullname}!")
    print(f"Your User ID is: {user_id}")
    db.close()

def login_user(username, password):
    db = connect_db()
    cursor = db.cursor()
    sql= "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, (username, password))
    user = cursor.fetchone()
    db.close()
    if user:
        print(f"Welcome back, {user[1]}!")
        return user[0]  # balikin user_id
    else:
        print("Invalid username or password")
        return None

def after_login_menu(user_id):
    while True:
        print("\n==== Menu MOODIE Digital Diary's ==== ")
        print("1. Add diary entry")
        print("2. View all diary")
        print("3. Add mood")
        print("4. Add achievement")
        print("5. View all achievements")
        print("6. Logout")
        choice = input("Choice Menu: ")

        if choice == "1":
            id_user = int(input("User ID: "))
            activities = input("Today's activities: ")
            add_diary_entry(id_user, activities)

        elif choice == "2":
            id_user = int(input("User ID: "))
            view_all_entries(id_user)

        elif choice == "3":
            id_user = int(input("User ID: "))
            tanggal = input("Tanggal: ")
            mood = input("Mood: ")
            add_mood(id_user, tanggal, mood)

        elif choice == "4":
            id_user = int(input("User ID: "))
            judul = input("Judul Achievement: ")
            deskripsi = input("Deskripsi: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            add_achievement(id_user, activities, deskripsi, judul)

        elif choice == "5":
            id_user = int(input("User ID: "))
            view_achievement(id_user)

        elif choice == "6":
            print("Goodbye!")
            break

# 2. diary entry
from datetime import datetime
def add_diary_entry(id_user,activities):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now()
    date = now.date()
    time = now.strftime("%Y-%m-%d %H:%M:%s")
    sql = "INSERT INTO diary_entry (id_user, todays_activities, date_time) VALUES (%s, %s, %s)"
    val = (id_user, activities, now)
    cursor.execute(sql, val)
    db.commit()
    print("Diary entry added successfully!")
    db.close()

def view_all_entries(id_user):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT id_entry, todays_activities, date_time FROM diary_entry WHERE id_user = %s"
    cursor.execute(sql, (id_user,))
    entries = cursor.fetchall()

    if entries:
        for entry in entries:
            print(f"No: {entry[0]}, Activities: {entry[1]}, DateTime: {entry[2]}")
    else:
            print("No diary entries")
    db.close()

def add_mood(id_user, mood):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().sfrftime("%Y-%m-%d %H:%M:%s")
    sql = "INSERT INTO mood (id_user, date_time, mood) VALUES (%s, %s, %s)"
    val = (id_user, now, mood)
    cursor.execute(sql, val)
    db.commit()
    print("Mood added successfully!")
    db.close()

def add_achievement(id_user, activities, deskripsi):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().sfrftime("%Y-%m-%d %H:%M:%s")
    sql = "INSERT INTO achievement (id_user activities, deskripsi, date_time) VALUES (%s, %s, %s)"
    val = (id_user, activities, deskripsi, now)
    cursor.execute(sql, val)
    db.commit()
    print("Achievement added successfully!")
    db.close()

def view_achievement(id_user):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT * FROM achievement WHERE id_user = %s"
    cursor.execute(sql, (id_user,))
    results = cursor.fetchall()
    if not results:
        print("No achievement")
    else:
        for achieve in results:
            print(f"No: {achieve[0]}, Title: {achieve[2]}, Description: {achieve[3]}, Date: {achieve[4]}")
    db.close()

def main():
    while True:
        print("\n=== Welcome to MOODIE - your mood & digital diary! ===")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Username: ")
            fullname = input("Fullname: ")
            password = input("Password: ")
            date_of_birth = input("Date of birth (YYYY-MM-DD): ")
            gender = input("Gender F/M: ")
            register_user(username, fullname, password, date_of_birth, gender)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = login_user(username, password)
            if user:
                after_login_menu(username)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

main()

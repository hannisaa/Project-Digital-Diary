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

current_user_id = None
def login_user(username, password):
    global current_user_id
    db = connect_db()
    cursor = db.cursor()
    sql= "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    user = cursor.fetchone()
    db.close()
    if user:
        current_user_id = user[0]
        print(f"Welcome back, {user[1]}!")
        print(f"Your User ID is: {current_user_id}")
        return current_user_id
    else:
        print("Invalid username or password")
        return None

def after_login_menu(user_id):
    while True:
        print("\n==== Menu MOODIE Digital Diary's ==== ")
        print("1. Add diary entry")
        print("2. View all diary")
        print("3. Add mood")
        print("4. View all mood")
        print("5. Add achievement")
        print("6. View all achievements")
        print("7. Logout")
        choice = input("Choice Menu: ")

        if choice == "1":
            id_user = int(input("User ID: "))
            activities = input("Today's activities: ")
            add_diary_entry(current_user_id, activities)

        elif choice == "2":
            view_all_entries(current_user_id)

        elif choice == "3":
            id_user = int(input("User ID: "))
            tanggal = input("Tanggal: ")
            mood = input("Mood: ")
            add_mood(current_user_id, tanggal, mood)

        elif choice == "4":
            view_all_mood(current_user_id)

        elif choice == "5":
            id_user = int(input("User ID: "))
            judul = input("Judul Achievement: ")
            deskripsi = input("Deskripsi: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            add_achievement(current_user_id, activities, deskripsi, judul)

        elif choice == "6":
            view_achievement(current_user_id)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again")

# 2. diary entry
from datetime import datetime
def add_diary_entry(user_id, activities):
    global current_user_id
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now()
    date = now.date()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO diary_entry (id_user, todays_activities, date_time) VALUES (%s, %s, %s)"
    val = (current_user_id, activities, now)
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

def update_diary_entry(user_id, entry_id, new_activities):
    db = connect_db()
    cursor = db.cursor()
    sql = "UPDATE diary_entry SET todays_activities = %s WHERE id_entry = %s AND id_user = %s"
    cursor.execute(sql, (new_activities, entry_id, user_id))
    db.commit()
    print("Diary updated successfully!")
    db.close()

def delete_diary_entry(user_id, entry_id):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM diary_entry WHERE id_entry = %s AND id_user = %s"
    cursor.execute(sql, (entry_id, user_id))
    db.commit()
    print("Diary entry deleted successfully!")
    db.close()

    if entries:
        for entry in entries:
            print(f"No: {entry[0]}, Activities: {entry[1]}, DateTime: {entry[2]}")
    else:
            print("No diary entries")
    db.close()

def add_mood(id_user, mood):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%s")
    sql = "INSERT INTO mood (id_user, date_time, mood) VALUES (%s, %s, %s)"
    val = (id_user, now, mood)
    cursor.execute(sql, val)
    db.commit()
    print("Mood added successfully!")
    db.close()

def view_all_mood(id_user):
    db = connect_db()
    cursor = db.cursor()
    sql = "SELECT id_mood, mood, date_time FROM mood WHERE id_user = %s"
    cursor.execute(sql, (id_user,))
    moods = cursor.fetchall()
    if moods:
        for mood in moods:
            print(f" No: {mood[0]}, MOOD: {mood[1]}, DateTime: {mood[2]}")

    else:
        print("No mood entries")
    db.close()

def add_achievement(id_user, activities, deskripsi):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%s")
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
            user_id = login_user(username, password)
            if user_id:
                after_login_menu(username)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

main()



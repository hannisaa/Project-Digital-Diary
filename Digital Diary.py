from enum import nonmember
from operator import truediv

import os
import mysql
from mysql.connector.constants import flag_is_set
from datetime import datetime


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db_digital_diary",
    )

current_user_id = None
current_username = None

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
    global current_user_id, current_username
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        print("User not found")
        return None
    if user["password"] == password:
        current_user_id = user["id_user"]
        current_username = user["username"]
        print(f"Welcome back, {current_username}")
        print(f"Your User ID is: {current_user_id}")
        return current_user_id
    else:
        print("Invalid username or password")
        return None


def forgot_password():
    db = connect_db()
    cursor = db.cursor()
    print("\n=== Forgot Password ===")
    username = input("Enter username: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    sql = "SELECT id_user, password FROM users WHERE username = %s AND date_of_birth = %s"
    cursor.execute(sql, (username, date_of_birth))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
        old_password = result[1]
        print(f"Your current password: {old_password}")
        choice = input("Do you want to update your password? (y/n): ").lower()
        if choice == 'y':
            new_password = input("Enter new password: ")
            sql_update = "UPDATE users SET password = %s WHERE id_user = %Zs"
            cursor.execute(sql_update, (new_password, user_id))
            db.commit()
            print("Password updated successfully!")
        else:
            print("Password not changed.")
    else:
        print("No matching user found. Please check your username and date of birth.")

    db.close()


def after_login_menu(user_id):
    while True:
        print("\n=== Menu Digital Diary's ===")
        print("1. Diary")
        print("2. Mood")
        print("3. Achievement")
        print("4. Logout")
        choice = input("Choice Menu: ")

        if choice == "1":
            diary_menu(user_id)

        elif choice == "2":
            mood_menu(user_id)

        elif choice == "3":
            achievement_menu(user_id)

        elif choice == "4":
            print("Goodbye, have a nice day!")
            break
        else:
            print("Invalid choice, please try again")

def diary_menu(user_id):
    while True:
        print("\n===  Diary Menu ===")
        print("1. Add diary entry")
        print("2. View all diary entries")
        print("3. Update diary entry")
        print("4. Delete diary entry")
        print("5. Back to main menu")
        choice = input("Choice: ")
        if choice == "1":
            activities = input("Today's activities: ")
            add_diary_entry(user_id, activities)
        elif choice == "2":
            view_all_entries(user_id)
        elif choice == "3":
            entry_id = input("Entry ID to update: ")
            new_activities = input("New activities: ")
            update_diary_entry(user_id, entry_id, new_activities)
        elif choice == "4":
            entry_id = input("Entry ID to delete: ")
            delete_diary_entry(user_id, entry_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def mood_menu(user_id):
    while True:
        print("\n=== Mood Menu ===")
        print("1. Add mood")
        print("2. View all mood entries")
        print("3. Update mood entry")
        print("4. Delete mood entry")
        print("5. Back to main menu")
        choice = input("Choice: ")
        if choice == "1":
            mood = input("Mood: ")
            add_mood(user_id, mood)
        elif choice == "2":
            view_all_mood(user_id)
        elif choice == "3":
            mood_id = input("Mood ID to update: ")
            new_mood = input("New mood: ")
            update_mood(user_id, mood_id, new_mood)
        elif choice == "4":
            mood_id = input("Mood ID to delete: ")
            delete_diary_entry(user_id, mood_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

def achievement_menu(user_id):
    while True:
        print("\n=== Menu Achievement ===")
        print("1. Add achievement")
        print("2. View all achievements")
        print("3. Update achievement entry")
        print("4. Delete achievement entry")
        print("5. Back to main menu")
        choice = input("Choice: ")
        if choice == "1":
            title = input("Title Achievement: ")
            description = input("Description: ")
            add_achievement(user_id, title, description)
        elif choice == "2":
            view_achievement(user_id)
        elif choice == "3":
            try:
                achievement_id = input("Achievement ID to update: ")
                new_title = input("New title: ")
                new_description = input("New desription: ")
                update_achievement(user_id, achievement_id, new_title, new_description)
            except ValueError:
                print("Invalid input. Achievement ID must be a number.")
        elif choice == "4":
            try:
                achievement_id = int(input("Achievement ID to delete: "))
                delete_achievement(user_id, achievement_id)
            except ValueError:
                print("Invalid input. Achievement ID must be a number.")
        elif choice == "5":
            break
        else:
            print("Invalid choice")




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
    if entries:
        print("\n=== Your Diary Entries ===")
        for entry in entries:
            print(f"NO: {entry[0]}, Activities: {entry[1]}, DateTime: {entry[2]}")
    else:
        print("No diary entries found.")

    db.close()

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
    sql = "SELECT id_entry, todays_activities, date_time FROM diary_entry WHERE id_user = %s"
    cursor.execute(sql, (user_id,))
    entries = cursor.fetchall()

    if entries:
        print("\n=== Your Remaining Diary Entries ===")
        for entry in entries:
            print(f"NO: {entry[0]}, Activities: {entry[1]}, DateTime: {entry[2]}")
    else:
        print("No diary entries left.")

    db.close()

# 3. Mood
def add_mood(id_user, mood):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO mood (id_user, date_time, mood) VALUES (%s, %s, %s)"
    val = (id_user, mood, now)
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
            print(f" No: {mood[0]}, Mood: {mood[1]}, DateTime: {mood[2]}")
    else:
        print("No mood entries")
    db.close()

def update_mood(user_id, mood_id, new_mood):
    db = connect_db()
    cursor = db.cursor()
    sql = "UPDATE mood SET mood = %s WHERE id_mood = %s AND id_user = %s"
    cursor.execute(sql, (new_mood, mood_id, user_id))
    db.commit()
    print("Mood updated successfully!")
    db.close()

def delete_mood(user_id, mood_id):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM mood WHERE id_mood = %s AND id_user = %s"
    cursor.execute(sql, (mood_id, user_id))
    db.commit()
    print("Mood entry deleted successfully!")
    sql = ("SELECT id_mood, mood, date_time FROM mood WHERE id_user = %s")
    cursor.execute(sql, (user_id,))
    moods = cursor.fetchall()
    if moods:
        print("\n=== Remaining Mood Entries ===")
        for mood in moods:
            print(f"NO: {mood[0]}, Activities: {mood[1]}, DateTime: {mood[2]}")
    else:
        print("No mood entries left.")
    db.close()

#3. achievement
def add_achievement(id_user, title, description):
    db = connect_db()
    cursor = db.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO achievement (id_user, title, description, date_time) VALUES (%s, %s, %s, %s)"
    val = (id_user, title, description, now)
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
        print("No achievement found")
    else:
        for achieve in results:
            print(f"No: {achieve[0]}, Title: {achieve[2]}, Description: {achieve[3]}, Date: {achieve[4]}")
    db.close()

def update_achievement(user_id, achievement_id, new_title, new_description):
    db = connect_db()
    cursor = db.cursor()
    sql = "UPDATE achievement SET title = %s, description = %s WHERE id_achievement = %s AND id_user = %s"
    cursor.execute(sql, (new_title, new_description, achievement_id, user_id))
    db.commit()
    if cursor.rowcount > 0:
        print("Achievement updated successfully!")
    else:
        print("No achievement found")
    db.close()

def delete_achievement(user_id, achievement_id):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM achievement WHERE id_achievement = %s AND id_user = %s"
    cursor.execute(sql, (achievement_id, user_id))
    db.commit()
    if cursor.rowcount > 0:
        print("Diary entry deleted successfully!")
    else:
        print("No achievement found")

    sql = "SELECT id_entry, todays_activities, date_time FROM diary_entry WHERE id_user = %s"
    cursor.execute(sql, (user_id,))
    achievement = cursor.fetchall()
    if achievement:
        print("\n=== Remaining achievement ===")
        for achieve in achievement:
            print(f"NO: {achieve[0]}, Activities: {achieve[1]}, DateTime: {achieve[2]}")
    else:
        print("No diary entries left.")
    db.close()

def main():
    while True:
        print("\n=== Welcome to MOODIE - your mood & digital diary! ===")
        print("1. Register User")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")

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
                after_login_menu(user_id)

        elif choice == "3":
            forgot_password()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

main()

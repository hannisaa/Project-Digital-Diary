import mysql.connector
from datetime import datetime


# ================= Database ==================
class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_digital_diary"
        )
        self.cursor = self.db.cursor(dictionary=True)

    def execute(self, sql, val=None):
        self.cursor.execute(sql, val)
        self.db.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.db.close()


# ================= User ==================
class User:
    def __init__(self, username=None, fullname=None, password=None, date_of_birth=None, gender=None):
        self.id_user = None
        self.username = username
        self.fullname = fullname
        self.password = password
        self.date_of_birth = date_of_birth
        self.gender = gender

    def register(self):
        db = Database()
        sql = """INSERT INTO users (username, fullname, password, date_of_birth, gender) 
                 VALUES (%s, %s, %s, %s, %s)"""
        val = (self.username, self.fullname, self.password, self.date_of_birth, self.gender)
        db.execute(sql, val)
        print(f"User {self.username} registered successfully!")
        db.close()

    def login_user(self, username, password):
        db = Database()
        db.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = db.fetchone()

        if not user:
            print("User not found")
            db.close()
            return False

        if user["password"] == password:
            self.id_user = user["id_user"]
            self.username = user["username"]
            self.fullname = user["fullname"]
            print(f"Welcome back, {self.fullname}! (ID: {self.id_user})")
            db.close()
            return True
        else:
            print("Invalid username or password")
            db.close()
            return False

    def forgot_password(self):
        db = Database()
        print("\n=== Forgot Password ===")
        username = input("Enter username: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")

        sql = "SELECT id_user, password FROM users WHERE username = %s AND date_of_birth = %s"
        db.cursor.execute(sql, (username, dob))
        result = db.fetchone()

        if result:
            print(f"Your current password: {result['password']}")
            choice = input("Do you want to update your password? (y/n): ").lower()
            if choice == 'y':
                new_pass = input("Enter new password: ")
                sql_update = "UPDATE users SET password = %s WHERE id_user = %s"
                db.execute(sql_update, (new_pass, result["id_user"]))
                print("Password updated successfully!")
            else:
                print("Password not changed.")
        else:
            print("No matching user found.")

        db.close()


# ================= Entry (Parent) ==================
class Entry:
    def __init__(self, user_id):
        self.user_id = user_id
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_entry(self):
        raise NotImplementedError


# ================= Diary ==================
class Diary(Entry):
    def __init__(self, user_id, activities=None):
        super().__init__(user_id)
        self.activities = activities

    def add_entry(self):
        db = Database()
        sql = "INSERT INTO diary_entry (id_user, todays_activities, date_time) VALUES (%s, %s, %s)"
        val = (self.user_id, self.activities, self.date_time)
        db.execute(sql, val)
        print("Diary entry added successfully!")
        db.close()

    def view_all(self):
        db = Database()
        sql = "SELECT id_entry, todays_activities, date_time FROM diary_entry WHERE id_user = %s"
        db.cursor.execute(sql, (self.user_id,))
        entries = db.fetchall()
        if entries:
            print("\n=== Your Diary Entries ===")
            for e in entries:
                print(f"ID: {e['id_entry']} | Activities: {e['todays_activities']} | Date: {e['date_time']}")
        else:
            print("No diary entries found.")
        db.close()

    def update(self, entry_id, new_activities):
        db = Database()
        sql = "UPDATE diary_entry SET todays_activities=%s WHERE id_entry=%s AND id_user=%s"
        db.execute(sql, (new_activities, entry_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Diary updated successfully!")
        else:
            print("No diary entry found.")
        db.close()

    def delete(self, entry_id):
        db = Database()
        sql = "DELETE FROM diary_entry WHERE id_entry=%s AND id_user=%s"
        db.execute(sql, (entry_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Diary entry deleted successfully!")
        else:
            print("No diary entry found.")
        db.close()


# ================= Mood ==================
class Mood(Entry):
    def __init__(self, user_id, mood=None):
        super().__init__(user_id)
        self.mood = mood

    def add_entry(self):
        db = Database()
        sql = "INSERT INTO mood (id_user, mood, date_time) VALUES (%s, %s, %s)"
        val = (self.user_id, self.mood, self.date_time)
        db.execute(sql, val)
        print("Mood added successfully!")
        db.close()

    def view_all(self):
        db = Database()
        sql = "SELECT id_mood, mood, date_time FROM mood WHERE id_user = %s"
        db.cursor.execute(sql, (self.user_id,))
        moods = db.fetchall()
        if moods:
            print("\n=== Your Mood Entries ===")
            for m in moods:
                print(f"ID: {m['id_mood']} | Mood: {m['mood']} | Date: {m['date_time']}")
        else:
            print("No mood entries found.")
        db.close()

    def update(self, mood_id, new_mood):
        db = Database()
        sql = "UPDATE mood SET mood=%s WHERE id_mood=%s AND id_user=%s"
        db.execute(sql, (new_mood, mood_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Mood updated successfully!")
        else:
            print("No mood entry found.")
        db.close()

    def delete(self, mood_id):
        db = Database()
        sql = "DELETE FROM mood WHERE id_mood=%s AND id_user=%s"
        db.execute(sql, (mood_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Mood entry deleted successfully!")
        else:
            print("No mood entry found.")
        db.close()


# ================= Achievement ==================
class Achievement(Entry):
    def __init__(self, user_id, title=None, description=None):
        super().__init__(user_id)
        self.title = title
        self.description = description

    def add_entry(self):
        db = Database()
        sql = "INSERT INTO achievement (id_user, title, description, date_time) VALUES (%s, %s, %s, %s)"
        val = (self.user_id, self.title, self.description, self.date_time)
        db.execute(sql, val)
        print("Achievement added successfully!")
        db.close()

    def view_all(self):
        db = Database()
        sql = "SELECT id_achieve, title, description, date_time FROM achievement WHERE id_user = %s"
        db.cursor.execute(sql, (self.user_id,))
        results = db.fetchall()
        if results:
            print("\n=== Your Achievements ===")
            for a in results:
                print(f"ID: {a['id_achieve']} | Title: {a['title']} | Description: {a['description']} | Date: {a['date_time']}")
        else:
            print("No achievements found.")
        db.close()

    def update(self, achieve_id, new_title, new_desc):
        db = Database()
        sql = "UPDATE achievement SET title=%s, description=%s WHERE id_achieve=%s AND id_user=%s"
        db.execute(sql, (new_title, new_desc, achieve_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Achievement updated successfully!")
        else:
            print("No achievement entry found.")
        db.close()

    def delete(self, achieve_id):
        db = Database()
        sql = "DELETE FROM achievement WHERE id_achieve=%s AND id_user=%s"
        db.execute(sql, (achieve_id, self.user_id))
        if db.cursor.rowcount > 0:
            print("Achievement deleted successfully!")
        else:
            print("No achievement entry found.")
        db.close()


# ================= Menu ==================
def after_login_menu(user):
    while True:
        print("\n=== Menu Digital Diary's ===")
        print("1. Diary")
        print("2. Mood")
        print("3. Achievement")
        print("4. Logout")
        choice = input("Choice: ")

        if choice == "1":
            diary_menu(user)
        elif choice == "2":
            mood_menu(user)
        elif choice == "3":
            achievement_menu(user)
        elif choice == "4":
            print("Goodbye, have a nice day!")
            break
        else:
            print("Invalid choice")


def diary_menu(user):
    diary = Diary(user.id_user)
    while True:
        print("\n=== Diary Menu ===")
        print("1. Add Diary")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        choice = input("Choice: ")

        if choice == "1":
            activities = input("Activities: ")
            diary = Diary(user.id_user, activities)
            diary.add_entry()
        elif choice == "2":
            diary.view_all()
        elif choice == "3":
            entry_id = input("Entry ID: ")
            new_act = input("New Activities: ")
            diary.update(entry_id, new_act)
        elif choice == "4":
            entry_id = input("Entry ID: ")
            diary.delete(entry_id)
        elif choice == "5":
            break


def mood_menu(user):
    mood = Mood(user.id_user)
    while True:
        print("\n=== Mood Menu ===")
        print("1. Add Mood")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        choice = input("Choice: ")

        if choice == "1":
            m = input("Mood: ")
            mood = Mood(user.id_user, m)
            mood.add_entry()
        elif choice == "2":
            mood.view_all()
        elif choice == "3":
            mood_id = input("Mood ID: ")
            new_m = input("New Mood: ")
            mood.update(mood_id, new_m)
        elif choice == "4":
            mood_id = input("Mood ID: ")
            mood.delete(mood_id)
        elif choice == "5":
            break


def achievement_menu(user):
    ach = Achievement(user.id_user)
    while True:
        print("\n=== Achievement Menu ===")
        print("1. Add Achievement")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Back")
        choice = input("Choice: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            ach = Achievement(user.id_user, title, desc)
            ach.add_entry()
        elif choice == "2":
            ach.view_all()
        elif choice == "3":
            aid = input("Achievement ID: ")
            new_t = input("New Title: ")
            new_d = input("New Description: ")
            ach.update(aid, new_t, new_d)
        elif choice == "4":
            aid = input("Achievement ID: ")
            ach.delete(aid)
        elif choice == "5":
            break


def main():
    while True:
        print("\n=== Welcome to MOODIE - your mood & digital diary! ===")
        print("1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Username: ")
            fullname = input("Fullname: ")
            password = input("Password: ")
            dob = input("Date of birth (YYYY-MM-DD): ")
            gender = input("Gender M/F: ")
            user = User(username, fullname, password, dob, gender)
            user.register()

        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = User()
            if user.login_user(username, password):
                after_login_menu(user)

        elif choice == "3":
            user = User()
            user.forgot_password()

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

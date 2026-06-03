# 📔 Digital Diary Management System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

A command-line Digital Diary application developed using **Python** and **MySQL** that allows users to record daily activities, moods, and achievements through a secure authentication system.

---

## 📌 Overview

Digital Diary is a personal journal management system that enables users to:

- Register and manage accounts
- Login securely
- Recover forgotten passwords
- Record daily diary entries
- Track moods
- Store achievements
- Update and delete records
- Maintain data persistence using MySQL

The project demonstrates the implementation of **Object-Oriented Programming (OOP)** concepts and database integration in a real-world CRUD application.

---

## 🚀 Features

### User Management

- User Registration
- User Login
- Forgot Password Recovery
- Logout Functionality

### Diary Management

- Add Diary Entry
- View Diary Entries
- Update Diary Entry
- Delete Diary Entry

### Mood Tracking

- Add Mood
- View Mood History
- Update Mood
- Delete Mood

### Achievement Tracking

- Add Achievement
- View Achievements
- Update Achievement
- Delete Achievement

---

## 🏗 System Architecture

The application is built using:

- Python
- MySQL
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)

---

## 🗄 Database Design

### Tables

#### Users

| Field | Type |
|---------|---------|
| id_user | Primary Key |
| username | VARCHAR |
| fullname | VARCHAR |
| password | VARCHAR |
| date_of_birth | DATE |
| gender | VARCHAR |

#### Diary Entries

| Field | Type |
|---------|---------|
| id_entry | Primary Key |
| user_id | Foreign Key |
| activity | TEXT |
| date_time | DATETIME |

#### Mood

| Field | Type |
|---------|---------|
| id_mood | Primary Key |
| id_user | Foreign Key |
| mood | VARCHAR |
| date_time | DATETIME |

#### Achievement

| Field | Type |
|---------|---------|
| id_achieve | Primary Key |
| id_user | Foreign Key |
| description | TEXT |
| date_time | DATETIME |

---

## 🔗 Entity Relationship Diagram

Add your ERD image here:

```md
![ERD](docs/ERD.png)
```

---

## 📂 Project Structure

```text
digital-diary-python-mysql/
│
├── README.md
│
├── src/
│   ├── main.py
│   ├── user.py
│   ├── diary.py
│   ├── mood.py
│   └── achievement.py
│
├── database/
│   └── db_digital_diary.sql
│
├── docs/
│   ├── ERD.png
│   ├── Flowchart.png
│   └── Project_Report.pdf
│
└── screenshots/
    ├── Login.png
    ├── Register.png
    ├── DiaryMenu.png
    └── AchievementMenu.png
```

---

## ⚙ Installation

### Prerequisites

- Python 3.10+
- MySQL Server
- XAMPP (optional)
- MySQL Connector for Python

Install dependency:

```bash
pip install mysql-connector-python
```

---

### Database Setup

Create a database:

```sql
CREATE DATABASE db_digital_diary;
```

Import:

```text
database/db_digital_diary.sql
```

---

### Run the Application

```bash
python main.py
```

---

## 📸 Screenshots

### Login Page

```md
![Login](screenshots/Login.png)
```

### Main Menu

```md
![Main Menu](screenshots/MainMenu.png)
```

### Diary Menu

```md
![Diary Menu](screenshots/DiaryMenu.png)
```

---

## 🎯 Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Python Programming
- MySQL Database Integration
- CRUD Operations
- User Authentication
- Relational Database Design
- Flowchart Design
- ERD Modeling

---

## 👨‍💻 Developers

- Hilwa Annisa
- Rizky Nur Aziz

---

## 🎓 Academic Project

Developed as part of the Python and SQL Programming course at CEP-CCIT, Faculty of Engineering, Universitas Indonesia.

---

## 📄 License

This project is intended for educational and portfolio purposes.

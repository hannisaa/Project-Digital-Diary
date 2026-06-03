# Implementation of Python and SQL Programming for a Digital Diary

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented%20Programming-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Selesai-brightgreen?style=for-the-badge)

##  Deskripsi Proyek

Digital Diary merupakan aplikasi berbasis **Python dan MySQL** yang dirancang untuk membantu pengguna mencatat aktivitas harian, suasana hati (mood), dan pencapaian pribadi secara digital.

Proyek ini mengimplementasikan konsep **Object-Oriented Programming (OOP)** serta integrasi database MySQL untuk menyimpan dan mengelola data pengguna secara terstruktur.

---

##  Tujuan Proyek

- Menerapkan konsep OOP dalam pengembangan aplikasi.
- Mengintegrasikan Python dengan MySQL.
- Mengimplementasikan operasi CRUD (Create, Read, Update, Delete).
- Membangun sistem autentikasi pengguna.
- Mendesain database relasional untuk kebutuhan aplikasi nyata.

---

##  Fitur Utama

###  Manajemen Pengguna

- Registrasi pengguna
- Login pengguna
- Lupa password
- Logout

###  Manajemen Diary

- Menambah catatan harian
- Melihat seluruh catatan
- Mengubah catatan
- Menghapus catatan

###  Manajemen Mood

- Menambah mood harian
- Melihat riwayat mood
- Mengubah mood
- Menghapus mood

###  Manajemen Achievement

- Menambah pencapaian
- Melihat daftar pencapaian
- Mengubah pencapaian
- Menghapus pencapaian

---

## Tools yang Digunakan

- Python
- MySQL
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)

---

##  Struktur Database

### Tabel

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

## Entity Relationship Diagram (ERD)

```md
![ERD](docs/ERD.png)
```

---

## Project Structure

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

## Installation

### Prerequisites

- Python 3.10+
- MySQL Server
- XAMPP 
- MySQL Connector for Python

## Cara Menjalankan Program

### 1. Install Dependensi

```bash
pip install mysql-connector-python
```

### 2. Buat Database

```sql
CREATE DATABASE db_digital_diary;
```

### 3. Import Database

Import file:

```text
database/db_digital_diary.sql
```

melalui phpMyAdmin atau MySQL Workbench.

### 4. Jalankan Program

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

## Konsep yang Diimplementasikan

- Object-Oriented Programming (OOP)
- CRUD Operations
- Database Relasional
- User Authentication
- MySQL Integration
- Flowchart Design
- Entity Relationship Diagram (ERD)

---

## Developers

- Hilwa Annisa
- Rizky Nur Aziz

---

## Academic Project

Proyek ini dikembangkan sebagai tugas mata kuliah Python dan SQL Programming di CEP-CCIT Fakultas Teknik Universitas Indonesia.

---

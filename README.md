
# 💰 Daily Money Tracker & Savings Insights API

A Django REST API backend for tracking daily income and expenses, analyzing savings performance, and generating financial insights.

Built as part of a ALX Capstone Project.

---

## 📌 Project Overview

The **Daily Money Tracker & Savings Insights API** is a backend system that allows users to:

* Register and authenticate securely using JWT
* Record income and expenses
* Categorize financial transactions
* View real-time financial summaries
* Receive rule-based savings insights and recommendations

The system is designed with a modular architecture and follows RESTful API principles.

---

## 🏗️ Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework**
* **Simple JWT (JWT Authentication)**
* SQLite (default database)

---

## 🧩 Project Architecture

The project is structured into four dedicated Django apps:

```
daily-money-tracker/
│
├── users/         # Authentication & user management
├── transactions/  # Income & expense tracking
├── dashboard/     # Financial summaries & calculations
├── insights/      # AI-style financial recommendations
└── manage.py
```

---

## 🔐 Authentication System

Authentication is handled using **JSON Web Tokens (JWT)**.

Users can:

* Register
* Log in
* Receive access and refresh tokens
* Access protected endpoints

All protected routes require a valid JWT token.

Unauthenticated access returns:

```
401 Unauthorized
```

---

## 💵 Core Features

### 1️⃣ Transaction Management

Users can:

* Add income or expense transactions
* Categorize transactions
* Record amount and date
* Retrieve their transaction history

### Transaction Model

* `type` (Income / Expense)
* `category`
* `amount`
* `date`
* `user`

---

### 2️⃣ Financial Dashboard

The dashboard endpoint dynamically calculates:

* Total Income
* Total Expenses
* Net Savings
* Savings Percentage

These calculations use Django ORM aggregation functions for efficiency.

Example Calculations:

```
Net Savings = Total Income - Total Expenses
Savings % = (Net Savings / Total Income) * 100
```

---

### 3️⃣ Smart Financial Insights

The insights system applies rule-based logic to generate recommendations:

* If savings > 20% → Suggest investment strategies
* If savings < 10% → Recommend expense reduction
* Balanced savings → Encourage financial discipline

These insights are stored using an `Insight` model.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MosesKariuki29/daily-money-tracker.git
cd daily-money-tracker
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## 🧪 API Testing

You can test endpoints using:

* Thunder Client (VS Code)
* Postman
* curl

Make sure to include:

```
Authorization: Bearer <access_token>
```

For protected routes.

---

## 📊 Example Workflow

1. Register user
2. Log in → receive JWT token
3. Add transactions
4. Access dashboard endpoint
5. Retrieve financial insights

---

## 🎯 Learning Outcomes

This project demonstrates:

* REST API design
* Django app modularization
* JWT authentication
* ORM aggregation
* Backend financial logic implementation
* Secure endpoint protection
* Git version control workflow

---

## 🔮 Future Improvements

* Frontend integration (React or Vue)
* Monthly analytics charts
* AI-powered financial predictions
* Budget goal tracking
* Deployment (Render / Railway / AWS)

---

## 👨‍💻 Author

**Moses Kariuki Mungai**
Computer Science Student
Murang’a University of Technology
Aspiring Software Developer (Fintech & Systems)

---

---


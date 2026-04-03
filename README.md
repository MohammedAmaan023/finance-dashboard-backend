# finance-dashboard-backend
Finance Dashboard Backend using Django REST Framework with JWT authentication, role-based access control, and CRUD APIs for financial records and analytics.

-----------------------------------------------------------
# 💰 Finance Dashboard Backend (Django + DRF)

## 📌 Project Overview

This project is a backend system for a **Finance Dashboard Application** where users can manage financial records based on their roles.

It supports:

* Role-based access control
* Financial records management
* Dashboard analytics
* JWT authentication

---

## 🚀 Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* SQLite (default Django DB)
* JWT Authentication (SimpleJWT)

---

## 🔐 Features

### 👤 User & Role Management

* Custom User Model with roles:

  * **Viewer** → Can view dashboard only
  * **Analyst** → Can view records & dashboard
  * **Admin** → Full access (CRUD + user management)
* Active/Inactive user status
* Role-based permissions implemented

---

### 💰 Financial Records Management

Each record contains:

* Amount
* Type (Income / Expense)
* Category
* Date
* Notes

Supported operations:

* Create record (Admin only)
* View records (Analyst/Admin)
* Update record (Admin only)
* Delete record (Admin only)
* Filter by:

  * Type
  * Category
  * Date range

---

### 📊 Dashboard APIs

Provides aggregated insights:

* Total Income
* Total Expense
* Net Balance
* Category-wise totals
* Recent transactions

---

### 🔐 Authentication

* JWT आधारित authentication
* Login endpoint returns:

  * Access token
  * Refresh token
* Secure API access using Bearer token

---

## 📡 API Endpoints

### 🔑 Authentication

| Method | Endpoint              | Description                |
| ------ | --------------------- | -------------------------- |
| POST   | `/api/token/`         | Get access & refresh token |
| POST   | `/api/token/refresh/` | Refresh access token       |

---

### 💰 Records

| Method | Endpoint                    | Access        |
| ------ | --------------------------- | ------------- |
| GET    | `/api/records/`             | Analyst/Admin |
| POST   | `/api/records/create/`      | Admin         |
| PUT    | `/api/records/<id>/`        | Admin         |
| DELETE | `/api/records/delete/<id>/` | Admin         |

---

### 📊 Dashboard

| Method | Endpoint          | Access        |
| ------ | ----------------- | ------------- |
| GET    | `/api/dashboard/` | Analyst/Admin |

---

### 👤 User Management

| Method | Endpoint           | Access |
| ------ | ------------------ | ------ |
| GET    | `/api/users/`      | Admin  |
| PUT    | `/api/users/<id>/` | Admin  |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/MohammedAmaan023/finance-dashboard-backend.git
cd finance-dashboard-backend
cd finance_project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔑 How to Use APIs

### Step 1: Get Token

```bash
POST /api/token/
```

### Step 2: Use Token

Add header:

```
Authorization: Bearer <access_token>
```

---

## 🧠 Design Decisions

* Used **Custom User Model** for role support
* Implemented **Role-Based Access Control** via custom permissions
* Used **JWT authentication** for secure APIs
* SQLite used for simplicity (assessment requirement)
* Clean separation of:

  * Models
  * Views
  * Serializers
  * Permissions

---

## ⚠️ Assumptions

* Single-user data isolation (records belong to logged-in user)
* Basic validation implemented
* No frontend included (backend-focused assignment)

---

## 🌟 Optional Enhancements (Future Scope)

* Pagination
* Search functionality
* Rate limiting
* Unit testing
* Swagger API docs

---

## 🏁 Conclusion

This project demonstrates:

* Strong backend design
* Clean API structure
* Secure authentication & authorization
* Real-world business logic implementation

---

## 👨‍💻 Author

**Mohammed Amaan**


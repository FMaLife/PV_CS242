# 📦 Project Setup Guide

## 🧰 1. Clone Repository

```bash
git clone https://github.com/ruvcandyfruit/CS254-242_68-2_Project-G09.git
cd CS254-242_68-2_Project-G09/backend
```

---

## 🐍 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```
> Before working next time, just ```cd backend``` and ```venv\Scripts\activate```
---

## 📥 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ 4. Setup Environment Variables

Create a `.env` file in `backend/`:

```env
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>
```

> Make sure you have PostgreSQL running.

---

## 🐘 5. Setup Database

### Create database in PostgreSQL

```bash
createdb mydb
```

---

## 🌱 6. Run Seed Script

Connect to database, create table, and insert data

```bash
python seed.py
```

---

## ▶️ 7. Run Application

```bash
python run.py
```

Server will start at:

```
http://127.0.0.1:5000
```

---

## 🔗 Testing login API in Postman

Method: **POST**

```
http://127.0.0.1:5000/api/auth/login
```

Choose Body -> raw -> JSON

```
{
    "email": "test@mail.com",
    "password": "1234"
}
```

Click **Send**, it choose show 200 OK and Cookie session

---

## 🍪 Notes (Session & CORS)

* Backend uses session-based authentication
* Make sure frontend sends:

```js
credentials: "include"
```

---

## ⚠️ Common Issues

### 1. CORS Error

Make sure backend has:

```python
CORS(app, supports_credentials=True)
```

---

### 2. Session Not Working

* Check `SECRET_KEY`
* Check frontend uses `credentials: "include"`

---

### 3. Database Connection Error

* Verify PostgreSQL is running
* Check `DATABASE_URL`

---


## 📌 Useful Commands

```bash
# after install new python library -> update requirements.txt
pip freeze > requirements.txt

# deactivate venv
deactivate
```

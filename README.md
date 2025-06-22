
---

# 🧪 Fitness Studio Booking API

A simple REST API to manage class bookings for a fitness studio. Built with **Django** and **Django REST Framework (DRF)**.

---

## 🚀 Features

* View all available fitness classes
* Book a slot for a class
* View bookings made by a client email
* Timezone-aware (IST default, stored in UTC)
* Prevents overbooking
* Clean REST API

---

## 🧰 Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework
* SQLite (default)
* Pytz for timezone conversion

---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/preyalameta02/omnify-fitness-booking.git
cd omnify-fitness-booking
```

### 2️⃣ Create virtual environment & activate

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser (optional, for Django Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Seed initial data

```bash
python studio/seed.py
```

### 7️⃣ Run the development server

```bash
python manage.py runserver
```

API will be available at:
`http://127.0.0.1:8000/`

---

## 🧪 API Endpoints

### 1️⃣ Get all classes

**Request:**

```bash
GET /classes/
```

**Curl Example:**

```bash
curl --location 'http://localhost:8000/classes'
```

**Sample Response:**

```json
[
  {
    "id": 1,
    "name": "Yoga",
    "datetime": "2025-06-25T01:30:00Z",
    "datetime_ist": "2025-06-25T07:00:00+05:30",
    "instructor": "Anjali",
    "available_slots": 10
  }
]
```

---

### 2️⃣ Make a booking

**Request:**

```bash
POST /book/

Content-Type: application/json

{
  "fitness_class": 5,
  "client_name": "Preyal",
  "client_email": "preyal@example.com"
}
```

**Curl Example:**

```bash
curl --location 'http://localhost:8000/book/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fitness_class": 5,
    "client_name": "Test User",
    "client_email": "test@example.com"
}'
```

**Responses:**

* ✅ **201 Created** — if booking is successful
* ❌ **400 Bad Request** — if no slots available or missing fields
* ❌ **404 Not Found** — if class ID is invalid

---

### 3️⃣ Get bookings by email

**Request:**

```bash
GET /bookings/?email=test@example.com
```

**Curl Example:**

```bash
curl --location 'http://localhost:8000/bookings?email=test%40example.com'
```

**Sample Response:**

```json
[
  {
    "id": 1,
    "fitness_class": 5,
    "client_name": "Test User",
    "client_email": "test@example.com",
    "booked_at": "2025-06-21T12:05:01.123456Z"
  }
]
```

---

## 🎯 Error Handling

* Prevents overbooking if slots are full
* Validates required fields (`fitness_class`, `client_name`, `client_email`)
* Validates class existence
* Handles invalid email queries

---

## 🕰 Timezone Handling

* All times are stored internally in **UTC**
* API returns original UTC time + a calculated IST time (`datetime_ist` field)

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🖥 Django Admin

You can also use Django Admin to:

* Manually add new classes
* View and manage bookings

Access at: `http://127.0.0.1:8000/admin/`

---

## 📬 Contact

If you have any questions feel free to contact me.
Email - ameta.preyal@gmail.com

---
# Piggy Integration

**Piggy Integration** is a Django backend designed to bridge the gap between Firebase services and non-mobile platforms, particularly **Desktop**, which does not support direct Firebase Authentication integration.

This backend ensures secure and consistent communication between the Piggy app and Firebase.

## 🎯 Purpose

Firebase Authentication and other services are limited on Desktop apps. This backend acts as a **middleware** that:

- Authenticates users via Firebase using REST.
- Syncs data securely between Firebase and the Piggy desktop app.
- Provides endpoints for user/session management.

## ⚙️ Tech Stack

- Python 3.11+
- Django 4.x
- Firebase Admin SDK
- Django REST Framework

## 🔐 Features

- 🔑 Firebase token verification
- 📦 API for handling secure communication with Piggy app
- ⚠️ No need to expose Firebase credentials on client side

## 🚀 Getting Started

### Installation

```bash
git clone git@github.com:Miga-Technologies/PiggyIntegration.git
cd piggy-integration
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Setup

Add your Firebase credentials JSON to the root directory.

`Set the path in your .env file or Django settings.`

### Run Server
```bash
python manage.py migrate
python manage.py runserver
```

### Endpoints

| Method | Endpoint          | Description                         | Auth Required |
| ------ | ----------------- | ----------------------------------- | ------------- |
| `POST` | `/auth/register/` | Register new user with Firebase UID | ❌             |
| `POST` | `/auth/login/`    | Authenticate using Firebase token   | ❌             |
| `GET`  | `/user/profile/`  | Get logged-in user's profile        | ✅             |
| `PUT`  | `/user/profile/`  | Update user profile                 | ✅             |
| `POST` | `/sync/data/`     | Sync app data to backend            | ✅             |
| `GET`  | `/sync/data/`     | Fetch user data from backend        | ✅             |
| `POST` | `/auth/refresh/`  | Refresh access token                | ✅             |
| `POST` | `/auth/logout/`   | Invalidate current user session     | ✅             |

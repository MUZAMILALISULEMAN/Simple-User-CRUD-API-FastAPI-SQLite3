# 🚀 FastAPI + SQLite3 CRUD API

A clean and modern backend project built with:

- 🔥 **FastAPI** for powerful API handling
- 🧠 **Pydantic** for data validation
- 🗃️ **SQLite3** as a simple embedded database
- 🐳 **Docker** to run it anywhere
- 🌐 **Frontend (HTML + JS)** for interacting with the API in real time

---

## 📦 Features

- Full CRUD operations (Create, Read, Update, Delete)
- User model with `name` and `age` fields
- SQLite database created on first run
- Cross-origin requests allowed (CORS ready for frontend)
- Beautiful frontend interface using plain HTML + JavaScript
- Dockerized backend — runs with one command

---

## 🎬 CRUD Operation Previews

Here’s a visual walkthrough of each core operation in the app:

---

### 🟢 Create User


  <img src="gifs/create.gif" alt="Create User" width="600"/>


---

### 🔵 Read Users


  <img src="gifs/read.gif" alt="Read Users" width="600"/>


---

### 🟡 Update User


  <img src="gifs/update.gif" alt="Update User" width="600"/>


---

### 🔴 Delete User


  <img src="gifs/delete.gif" alt="Delete User" width="600"/>


---



## 🧪 API Endpoints

| Method | Endpoint                  | Description                  |
|--------|---------------------------|------------------------------|
| POST   | `/response/`              | Create a new user            |
| GET    | `/users`                  | Get all users                |
| GET    | `/users/{id}`             | Get user by ID               |
| DELETE | `/del-user/{id}`          | Delete user by ID            |
| PUT    | `/update-user/{id}`       | Update user's name and age   |

---




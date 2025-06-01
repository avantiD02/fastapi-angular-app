## 📝 FastAPI + Angular ToDo App

This is a full-stack ToDo application built with **FastAPI** (Python) for the backend and **Angular** for the frontend. It allows users to add, view, and delete tasks, with data stored in a MySQL database.

---

## 🚀 Features

- ✅ Add new tasks
- ✅ View all tasks
- ✅ Delete tasks
- 🔄 Live reloading (FastAPI with `uvicorn --reload`)
- 📦 Angular standalone components
- 🔒 CORS configured for frontend-backend interaction

---

## 🛠️ Tech Stack

- **Frontend**: Angular
- **Backend**: FastAPI
- **Database**: MySQL
- **Others**: python-dotenv, CORS middleware, MySQL Connector

---

## 🔧 Setup Instructions

### ✅ Prerequisites

- Python 3.10+
- Node.js and Angular CLI
- MySQL server

---

### Backend Setup (FastAPI)

1. Navigate to the backend folder:
   ```bash
   cd backend

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Create a .env file in the backend folder

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload

The backend will run at: http://127.0.0.1:8000



### Frontend Setup (Angular)

1. Navigate to the Angular app directory:
   ```bash
   cd frontend/todo-app

2. Install dependencies:
   ```bash
   npm install

3. Run the Angular development server:
   ```bash
   ng serve

The frontend will run at: http://localhost:4200


### API Endpoints

| Method | Endpoint       | Description        |
|--------|----------------|--------------------|
| GET    | `/get_tasks`   | Fetch all tasks    |
| POST   | `/add_task`    | Add a new task     |
| POST   | `/delete_task` | Delete a task      |


### TODO (Future Improvements)

 Dockerize the project

 Add update/edit task feature

 Add authentication

 Deploy to Vercel / Render / Railway


### Author
Avanti Deshpande - 
Full Stack Developer

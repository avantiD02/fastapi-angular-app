from fastapi import APIRouter, Form 
from services import todo_service

router = APIRouter()

@router.get("/get_tasks")
def get_tasks():
    return todo_service.get_all_tasks()

@router.post("/add_task")
def add_task(task:str = Form(...)):
    todo_service.add_task(task)
    return "Task added successfully"

@router.post("/delete_task")
def delete_task(id:int = Form(...)):
    todo_service.delete_task(id)
    return "Task deleted successfully"
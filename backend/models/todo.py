from pydantic import BaseModel

class Task(BaseModel):
    id: int
    task: str
    
class AddTaskRequest(BaseModel):
    task: str

class DeleteTaskRequest(BaseModel):
    id: int
"""FastAPI example app - todo."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import todo
from dotenv import load_dotenv


# load environment variables from .env
load_dotenv()

# instantiate the FastAPI module
app = FastAPI()

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"], 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# include routers
app.include_router(todo.router)


@app.get('/')
def root():
    return {"message":"Hello World"}

# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Привет!"
    }

# uvicorn create_api_01:app --reload
# открываем http://127.0.0.1:8000

@app.get("/hello")
def hello():
    return {
        "message": "Hello API"
    }

# открываем http://127.0.0.1:8000/hello

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id
    }

# открываем http://127.0.0.1:8000/users/1

@app.get("/search")
def search(name: str):
    return {
        "name": name
    }

# открываем http://127.0.0.1:8000/search?name=Владимир

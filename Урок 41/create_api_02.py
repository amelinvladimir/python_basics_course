from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/")
def home():
    return {
        "message": "API работает"
    }


@app.post("/users")
def create_user(user: dict):
    users.append(user)

    return {
        "status": "created"
    }


@app.get("/users")
def get_users():
    return users

# uvicorn create_api_02:app --reload
# http://127.0.0.1:8000/users
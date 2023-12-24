from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/tasks/")
async def say_hello():
    return {"message": f"Tasks"}


@app.get("/api/v1/tasks/{task_id}")
async def say_hello(task_id: int):
    return {"message": f"Task {task_id}"}


@app.get("/api/v1/users/")
async def say_hello():
    return {"message": f"Users"}


@app.get("/api/v1/tasks/{user_id}")
async def say_hello(user_id: int):
    return {"message": f"User {user_id}"}
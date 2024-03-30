from fastapi import FastAPI
from .models import Todo
from .database import engine
from sqlmodel import Session,select
from typing import Optional

app = FastAPI()

session = Session(bind=engine)


@app.get("/todos")
async def get_all_todos():
    statement = select(Todo)
    results= session.exec(statement).all()
    return results

@app.post("/todos")
async def create_a_todo(todo:Todo):
    new_todo = Todo(title=todo.title,description=todo.description)
    session.add(new_todo)
    session.commit()
    return new_todo

@app.get("/todos/{todo_id}")
async def get_all_todo(todo_id:int):
    statement = select(Todo).where(Todo.id == todo_id)
    result = session.exec(statement)
    return result

@app.put("/todos/{todo_id}")
async def get_all_todos(todo_id:int):
    pass

@app.delete("/todos/{todo_id}")
async def delete_a_todo(todo_id:int):
    statement = select(Todo).where(Todo.id == todo_id)
    result = session.exec(statement).one_or_none()
    if result == None:
        return {"id":"not found"}
    session.delete(result)
    return result


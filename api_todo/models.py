from sqlmodel import SQLModel , Field
from pydantic import BaseModel
from typing import Optional


class Todo(SQLModel, table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    title:str
    description:str
    
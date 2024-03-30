from sqlmodel import SQLModel
from models import Todo
from database import engine

print("creating database .... ")


SQLModel.metadata.create_all(engine)

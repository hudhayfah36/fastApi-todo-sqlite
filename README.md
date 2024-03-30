## FastAPI Todo Application Documentation

This markdown file documents a basic todo application API built with FastAPI. It utilizes SQLite as the database for storing todo items. The API allows users to:

* **Get all** existing todo items.
* **Add** a new todo item with a title and description.
* **Update** an existing todo item (title and/or description).
* **Delete** a todo item.

### Dependencies

This API uses the following libraries:

* FastAPI
* Pydantic (for data validation)
* SQLAlchemy (for database interaction)

### Database Setup

The application uses SQLite for data storage. You will need to configure a connection string in your application code pointing to your desired database file.

### Models

The API utilizes Pydantic models to define the schema for todo items:

```python
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False

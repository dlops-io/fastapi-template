from pydantic import BaseModel


class EditToDo(BaseModel):
    task: str
    priority: int


class ToDo(EditToDo):
    id: int

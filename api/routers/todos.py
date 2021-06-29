from fastapi import APIRouter, Path
from api.schemas import ToDo, EditToDo

router = APIRouter()

todos = [
    {'task': "Task A", 'priority': 1, 'id': 1},
    {'task': "Task B", 'priority': 1, 'id': 2},
    {'task': "Task C", 'priority': 2, 'id': 3}
]


@router.get(
    "/todos",
    tags=["To Dos"],
    summary="Get list of todos",
    description="Get list of todos"
)
async def todos_index():

    return todos


@router.post(
    "/todos",
    tags=["To Dos"],
    summary="Create a new todo",
    description="Create a new todo",
    response_description="The created todo"
)
async def todos_create(
    todo: EditToDo
):
    new_todo = {
        "id": len(todos)+1,
        "task": todo.task,
        "priority": todo.priority
    }
    todos.append(new_todo)

    return todo


@router.put(
    "/todos/{id}",
    tags=["To Dos"],
    summary="Update a todo",
    description="Update a todo using the provided metadata.",
    response_description="The updated todo"
)
async def todos_update(
        todo: ToDo,
        id: int = Path(..., description="The todo id")
):

    return todo


@router.get(
    "/todos/{id}",
    tags=["To Dos"],
    summary="Get information about a todo",
    description="Get all information about a specific todo.",
    response_description="The todo"
)
async def todos_fetch(
        id: int = Path(..., description="The todo id")
):
    # Find the todo
    todo = {}

    return todo

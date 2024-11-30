"""

Task Fixtures Modules

Holds fixtures of `Task`, `TaskList`, and `TaskManager` objects.
"""

from typing import List
import pytest

from app.task import Task
from app.task_list import TaskList


@pytest.fixture
def basic_task() -> Task:
    """Return a basic `Task` object with only a title set.
    
    Args:
        title (str): Custom title to use. Defaults to "Title"
    """
    def _basic_task(title: str = "Title"):
        return Task(title)

    return _basic_task


@pytest.fixture
def populated_task() -> Task:
    """Return a `Task` object with a fully populated set of attribute values.
    
    Args:
        title (str): Custom title to use. Defaults to "Title"
    """
    def _populated_task(title: str = "Title"):
        return Task(
            title=title,
            description="Task description.",
            due_date="10/10/2024",
            status="in progress",
        )

    return _populated_task


@pytest.fixture
def list_of_tasks(populated_task) -> List[Task]:
    def _list_of_tasks(count: int = 3):
        tasks = []
        if count > 0:
            for i in range(count):
                tasks.append(populated_task(title=f"Task {i}"))
        return tasks

    return _list_of_tasks


@pytest.fixture
def empty_task_list() -> TaskList:
    return TaskList()


@pytest.fixture
def filled_task_list(list_of_tasks) -> TaskList:
    def _filled_task_list(count: int = 3):
        return TaskList(task_list=list_of_tasks(count))

    return _filled_task_list

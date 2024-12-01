"""

Task Fixtures Modules

Holds fixtures of `Task`, `TaskList`, and `TaskManager` objects.
"""

from datetime import datetime
from typing import List
import pytest

from app.task import Task
from app.task_list import TaskList
from app.task_manager import TaskManager


# TASK ATTRIBUTE FIXTURE PARAMS ====================================================================
@pytest.fixture(
    params=[
        "Complete project report",
        "Buy groceries",
        "Meeting with team at 10 AM",
        "Fix bug #123",
        "Call John about contract renewal",
        "Prepare presentation slides",
        "Book dentist appointment",
        "Submit timesheet",
        "Research new marketing strategies",
        "Organize workspace",
    ]
)
def valid_task_titles(request):
    return request.param


@pytest.fixture(
    params=[
        "",
        "   ",
        None,
        "\t\n",
        "   \n",
        " ",
    ]
)
def invalid_task_titles(request):
    return request.param


@pytest.fixture(
    params=[
        "Complete the project documentation",
        "Buy groceries and household supplies",
        "Schedule a team meeting for next week",
        "Fix bug #123 in the codebase",
        "Prepare slides for the upcoming presentation",
        "",
        None,
        " ",
        "\nWrite unit tests for new feature\n",
        "Follow up with client on feedback",
    ]
)
def valid_task_descriptions(request):
    return request.param


@pytest.fixture(
    params=["pending", "in progress", "completed", "Pending", "IN PROGRESS"]
)
def valid_task_statuses(request):
    return request.param


@pytest.fixture(
    params=[
        "done",
        "started",
        "not started",
        "waiting",
        "finished",
        "",
        " ",
        None,
        "complete",
        "inprogress",
    ]
)
def invalid_task_statuses(request):
    return request.param


@pytest.fixture(
    params=[
        "01/01/2024",
        "12/31/2024",
        "3/15/2025",
        "07/04/2024",
        "7/4/2024",
        "11/11/2024",
        datetime(2024, 1, 1),
        datetime(2025, 12, 31),
        datetime(2023, 6, 10),
        datetime(2024, 11, 25),
        datetime(2024, 5, 20),
    ]
)
def valid_task_due_dates(request):
    return request.param


@pytest.fixture(
    params=[
        "2024-01-01",
        "January 1, 2024",
        "1/1/24",
        "2024/01/01",
        "01-01-2024",
        "13/01/2024",
        "02/30/2024",
        "02/01/24",
        " ",
        "",
        None,
    ]
)
def invalid_task_due_dates(request):
    return request.param


# TASK OBJECT FIXTURES =============================================================================


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


# TASK LISTS AND TASKLIST OBJECT FIXTURES ==========================================================
@pytest.fixture
def list_of_tasks(populated_task) -> List[Task]:
    """Return a list populated with a number of fully-populated tasks with unique titles.

    Args:
        count (int): Number of tasks to put in list. Defaults to 3.
    """

    def _list_of_tasks(count: int = 3):
        tasks = []
        if count > 0:
            for i in range(count):
                tasks.append(populated_task(title=f"Task {i}"))
        return tasks

    return _list_of_tasks


@pytest.fixture
def empty_task_list() -> TaskList:
    """Return a `TaskList` object with no tasks in its `task_list`."""
    return TaskList()


@pytest.fixture
def populated_task_list(list_of_tasks) -> TaskList:
    """Return a `TaskList` object with an internal `task_list` filled with a  number of fully-
    populated tasks (each with a unique title).

    Args:
        count (int): Number of tasks to put in list. Defaults to 3.
    """

    def _populated_task_list(count: int = 3):
        return TaskList(task_list=list_of_tasks(count))

    return _populated_task_list


# TASK MANAGER OBJECT FIXTURES =====================================================================


@pytest.fixture
def empty_task_manager(list_of_tasks) -> TaskManager:
    """Return a `TaskManager` object, whose held `TaskList` contains no tasks."""

    def _populated_task_manager(count: int = 3):
        return TaskManager(task_list=TaskList(task_list=list_of_tasks(count)))

    return _populated_task_manager


@pytest.fixture
def populated_task_manager(list_of_tasks) -> TaskManager:
    """Return a `TaskManager` object, whose held `TaskList` contains a list of tasks (each with
    unique titles).

    Args:
        count (int): Number of tasks to put in list. Defaults to 3.
    """

    def _populated_task_manager(count: int = 3):
        return TaskManager(task_list=TaskList(task_list=list_of_tasks(count)))

    return _populated_task_manager

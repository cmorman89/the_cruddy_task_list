"""
Tests for the `Task` Module
"""

from datetime import datetime

import pytest

from app.task import Task, TaskError, BlankTitleError


@pytest.mark.parametrize(
    "title, description, due_date, status, exp_due_date, exp_status",
    [
        ("Task Title", None, None, None, "", "Pending"),
        (
            "Task Title",
            "The longer description of the task.",
            datetime(2024, 12, 31),
            "Completed",
            datetime(2024, 12, 31),
            "Completed",
        ),
    ],
)
def test_task_construction(
    title, description, due_date, status, exp_due_date, exp_status
):
    """Test basic `Task` construction, including minimal and full arguments provided"""
    task = Task(title=title, description=description, due_date=due_date, status=status)
    assert task.task_id >= 0
    assert task.title == title
    assert task.description == description if description else task.description is None
    if due_date:
        assert task.due_date == exp_due_date
    else:
        assert isinstance(task.due_date, datetime)
    assert task.status == exp_status


def test_task_id_uniqueness():
    """Generate several `Task` objects and check that each ID is unique."""
    task_1 = Task("task 1")
    task_2 = Task("task 2")
    task_3 = Task("task 3")

    assert task_1.task_id != task_2.task_id != task_3.task_id


def test_task_id_immutable():
    """Test that `task_id` cannot be set from public interface after init"""
    task = Task("task")
    try:
        task.task_id = 1
    except AttributeError:
        assert True


def test_task_title_setter():
    """Test attempting to construct and then set a task title to valid and invalid titles."""
    valid_task_titles = [
        "Title",
        "1234",
        "1",
        "a",
        "A longer title with some punctuation.",
    ]
    invalid_task_titles = [None, "", "     ", "\n", "\t"]

    for valid_title in valid_task_titles:
        # Test valid title via constructor
        task = Task(title=valid_title)
        assert task.title == valid_title

        # Test valid title via setter
        task = Task(title="Title")
        task.title = valid_title
        assert task.title == valid_title

    for invalid_title in invalid_task_titles:
        # Test invalid title via constructor
        print(invalid_title)
        with pytest.raises(TaskError) as e:
            task = Task(title=invalid_title)
            print(f"Invalid Title={invalid_title}, task={task}")
        assert isinstance(e.value, BlankTitleError)

        # Test invalid title via setter
        task = Task(title="Title")
        with pytest.raises(TaskError) as e:
            task.title = invalid_title
        assert isinstance(e.value, BlankTitleError)


@pytest.mark.parametrize(
    "status, exp_status",
    [
        (None, "Pending"),
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("In Progress", "In Progress"),
        ("Pending".lower(), "Pending"),
        ("Completed".lower(), "Completed"),
        ("In Progress".lower(), "In Progress"),
        ("Pending".upper(), "Pending"),
        ("Completed".upper(), "Completed"),
        ("In Progress".upper(), "In Progress"),
        ("", "Pending"),
        ("Finished", "Pending"),
        ("Incomplete", "Pending"),
    ],
)
def test_task_status_setter(status, exp_status):
    """Test valid and invalid statuses, as well as edge cases and string case handling"""
    task = Task(title="Title", status=status)
    assert task.status == exp_status


def test_task_str_method():
    """Test the string representation of a task"""
    title = "Title"
    description = "Description"
    due_date = datetime.now()
    status = "Completed"
    task = Task(title=title, description=description, due_date=due_date, status=status)
    task_id = task.task_id
    expected_str = f"{title} (ID #{task_id})"

    assert str(task) == expected_str


def test_task_repr_method():
    """Test the full representation of a task"""
    title = "Title"
    description = "Description"
    due_date = datetime.now()
    status = "Completed"
    task = Task(title=title, description=description, due_date=due_date, status=status)
    task_id = task.task_id
    expected_str = (
        f'<Task: task_id="{task_id}", '
        f'title="{title}", '
        f'description="{description}", '
        f"due_date={due_date.strftime("%Y-%m-%d %H:%M")}, "
        f'status="{status}">'
    )

    assert f"{task!r}" == expected_str

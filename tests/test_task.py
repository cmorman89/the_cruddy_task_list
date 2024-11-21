"""
Tests for the `Task` Module
"""

from datetime import datetime

import pytest

from app.task import Task


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

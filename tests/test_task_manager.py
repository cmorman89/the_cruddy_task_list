"""
Tests for the `task_manager.py` module
"""

from datetime import datetime

from app.task_manager import TaskManager


def test_task_manager_constructor(empty_task_list):
    """Test if a basic `TaskManager` can be successfully initialized."""
    task_manager = TaskManager(task_list=empty_task_list)
    assert isinstance(task_manager, TaskManager)


def test_set_valid_task_title(populated_task_manager, valid_task_titles):
    """Test setting the title of the first task in a task list to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_title(idx, valid_task_titles)
    assert task_manager.get_task_by_index(idx).title == valid_task_titles


def test_set_valid_task_description(populated_task_manager, valid_task_descriptions):
    """Test setting the description of the first task in a task list to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_description(idx, valid_task_descriptions)
    assert task_manager.get_task_by_index(idx).description == valid_task_descriptions


def test_set_valid_task_status(populated_task_manager, valid_task_statuses):
    """Test setting the status of the first task in a task list to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_status(idx, valid_task_statuses)
    assert task_manager.get_task_by_index(idx).status == valid_task_statuses.lower()


def test_set_valid_task_due_date(populated_task_manager, valid_task_due_dates):
    """Test setting the due date of the first task in a task list to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_due_date(idx, valid_task_due_dates)
    assert (
        task_manager.get_task_by_index(idx).due_date == valid_task_due_dates
        if isinstance(valid_task_due_dates, datetime)
        else datetime.strptime(valid_task_due_dates, "%m/%d/%Y")
    )

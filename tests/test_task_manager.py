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
    """Test if `TaskManager` can fetch a task and change its title to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_title(idx, valid_task_titles)
    assert task_manager.get_task_by_index(idx).title == valid_task_titles


def test_set_valid_task_description(populated_task_manager, valid_task_descriptions):
    """Test if `TaskManager` can fetch a task and change its description to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_description(idx, valid_task_descriptions)
    assert task_manager.get_task_by_index(idx).description == valid_task_descriptions


def test_set_valid_task_status(populated_task_manager, valid_task_statuses):
    """Test if `TaskManager` can fetch a task and change its status to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_status(idx, valid_task_statuses)
    assert task_manager.get_task_by_index(idx).status == valid_task_statuses.lower()


def test_set_valid_task_due_date(populated_task_manager, valid_task_due_dates):
    """Test if `TaskManager` can fetch a task and change its status to a valid input."""
    idx = 0
    task_manager = populated_task_manager()
    task_manager.set_task_due_date(idx, valid_task_due_dates)
    assert (
        task_manager.get_task_by_index(idx).due_date == valid_task_due_dates
        if isinstance(valid_task_due_dates, datetime)
        else datetime.strptime(valid_task_due_dates, "%m/%d/%Y")
    )


def test_get_task(populated_task_manager):
    task_manager: TaskManager = populated_task_manager(count=5)
    task_idx = 3
    task = task_manager.task_list.task_list[task_idx]
    assert task_manager.get_task(task_idx) == task
    assert task_manager.get_task(task.task_id) == task
    assert task_manager.get_task(task) == task


def test_get_task_by_index(populated_task_manager):
    count = 5
    task_manager: TaskManager = populated_task_manager(count=count)
    for i, task in enumerate(task_manager.task_list.task_list):
        assert task_manager.get_task_by_index(i) == task


def test_get_task_by_id(populated_task_manager):
    count = 5
    task_manager: TaskManager = populated_task_manager(count=count)
    for i, task in enumerate(task_manager.task_list.task_list):
        assert task_manager.get_task_by_id(task.task_id) == task


def test_add_task_to_list(empty_task_manager, list_of_tasks):
    count = 3
    task_manager: TaskManager = empty_task_manager
    for task in list_of_tasks(count=count):
        task_manager.add_task_to_list(task)
    assert len(task_manager.task_list.task_list) == count


def test_delete_task_from_list(populated_task_manager):
    task_manager: TaskManager = populated_task_manager()
    for task in task_manager.task_list.task_list:
        task_manager.delete_task_from_list(task)

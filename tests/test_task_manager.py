import pytest

from app.task import Task
from app.task_manager import (
    AddDuplicateTaskError,
    EmptyTaskListError,
    TaskManager,
    TaskManagerError,
    TaskNotFoundError,
)


def test_task_manager_constructor():
    "Test basic construction with and without a task list provided."
    task_manager = TaskManager()
    assert not task_manager.task_list

    task_list = [Task("task 1"), Task("task 2"), Task("task 3")]
    task_manager = TaskManager(task_list=task_list)
    assert task_manager.task_list == task_list


def test_add_task():
    """Test adding multiple new (valid) and duplicate (invalid) tasks."""
    task_manager = TaskManager()
    task_list = [Task("task 1"), Task("task 2"), Task("task 3")]

    # Add the tasks the first time
    for task in task_list:
        task_manager.add_task(task)
    assert task_manager.task_list == task_list

    # Try adding them again (error state)
    for task in task_list:
        with pytest.raises(TaskManagerError) as e:
            task_manager.add_task(task)
        assert isinstance(e.value, AddDuplicateTaskError)


def test_get_task():
    """Test getting a task from a task list when it exists (valid), does not exists (invalid), and
    the list is empty (invalid).
    """
    task_manager = TaskManager()
    task_list = [Task("task 1"), Task("task 2"), Task("task 3")]
    valid_id = task_list[0].task_id
    invalid_id = Task("Not Added").task_id

    # Try to get a task from an empty list (error state)
    with pytest.raises(TaskManagerError) as e:
        task_manager.get_task(valid_id)
    assert isinstance(e.value, EmptyTaskListError)
    with pytest.raises(TaskManagerError) as e:
        task_manager.get_task(invalid_id)
    assert isinstance(e.value, EmptyTaskListError)

    # Get an existing task from the list.
    task_manager = TaskManager(task_list=task_list)
    assert task_manager.get_task(valid_id).task_id == valid_id

    # Try to get a task that does not exist in the list.
    with pytest.raises(TaskManagerError) as e:
        task_manager.get_task(invalid_id)
    assert isinstance(e.value, TaskNotFoundError)


def test_get_all_tasks():
    """Test getting all tasks from  a populated and an empty task list"""
    task_manager = TaskManager()
    assert not task_manager.get_all_tasks()

    task_list = [Task("task 1"), Task("task 2"), Task("task 3")]
    task_manager = TaskManager(task_list=task_list)
    assert task_manager.get_all_tasks() == task_list


def test_delete_task():
    """Test getting a task from a task list when it exists (valid), does not exists (invalid), and
    the list is empty (invalid).
    """
    task_manager = TaskManager()
    task_list = [Task("task 1"), Task("task 2"), Task("task 3")]
    valid_task = task_list[-1]
    valid_id = task_list[0].task_id
    invalid_task = Task("Not Added")
    invalid_id = invalid_task.task_id

    # Try to delete a task from an empty list (error state)
    with pytest.raises(TaskManagerError) as e:
        task_manager.delete_task(valid_id)
    assert isinstance(e.value, EmptyTaskListError)

    with pytest.raises(TaskManagerError) as e:
        task_manager.delete_task(invalid_id)
    assert isinstance(e.value, EmptyTaskListError)

    # Delete an existing task from the list by ID and by a `Task` object
    task_manager = TaskManager(task_list=task_list)
    task_manager.delete_task(task=valid_id)
    task_manager.delete_task(task=valid_task)

    # Try to get a task that does not exist in the list.
    with pytest.raises(TaskManagerError) as e:
        task_manager.delete_task(invalid_id)
    assert isinstance(e.value, TaskNotFoundError)

    with pytest.raises(TaskManagerError) as e:
        task_manager.delete_task(invalid_task)
    assert isinstance(e.value, TaskNotFoundError)

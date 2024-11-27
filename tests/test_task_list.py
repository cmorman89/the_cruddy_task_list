"""
Task List Testing Module
"""

import pytest

from app.task import Task
from app.task_list import (
    AddDuplicateTaskError,
    EmptyTaskListError,
    TaskList,
    TaskListError,
    TaskNotFoundError,
)


def test_task_list_constructor():
    "Test basic construction with and without a task list provided."
    task_list = TaskList()
    assert not task_list.task_list

    list_of_tasks = [Task("task 1"), Task("task 2"), Task("task 3")]
    task_list = TaskList(task_list=list_of_tasks)
    assert task_list.task_list == list_of_tasks


def test_add_task():
    """Test adding multiple new (valid) and duplicate (invalid) tasks."""
    task_list = TaskList()
    list_of_tasks = [Task("task 1"), Task("task 2"), Task("task 3")]

    # Add the tasks the first time
    for task in list_of_tasks:
        task_list.add_task(task)
    assert task_list.task_list == list_of_tasks

    # Try adding them again (error state)
    for task in list_of_tasks:
        with pytest.raises(TaskListError) as e:
            task_list.add_task(task)
        assert isinstance(e.value, AddDuplicateTaskError)


def test_get_task():
    """Test getting a task from a task list when it exists (valid), does not exists (invalid), and
    the list is empty (invalid).
    """
    task_list = TaskList()
    list_of_tasks = [Task("task 1"), Task("task 2"), Task("task 3")]
    valid_id = list_of_tasks[0].task_id
    invalid_id = Task("Not Added").task_id

    # Try to get a task from an empty list (error state)
    with pytest.raises(TaskListError) as e:
        task_list.get_task(valid_id)
    assert isinstance(e.value, EmptyTaskListError)
    with pytest.raises(TaskListError) as e:
        task_list.get_task(invalid_id)
    assert isinstance(e.value, EmptyTaskListError)

    # Get an existing task from the list.
    task_list = TaskList(task_list=list_of_tasks)
    assert task_list.get_task(valid_id).task_id == valid_id

    # Try to get a task that does not exist in the list.
    with pytest.raises(TaskListError) as e:
        task_list.get_task(invalid_id)
    assert isinstance(e.value, TaskNotFoundError)


def test_get_all_tasks():
    """Test getting all tasks from  a populated and an empty task list"""
    task_list = TaskList()
    assert not task_list.get_all_tasks()

    list_of_tasks = [Task("task 1"), Task("task 2"), Task("task 3")]
    task_list = TaskList(task_list=list_of_tasks)
    assert task_list.get_all_tasks() == list_of_tasks


def test_delete_task():
    """Test getting a task from a task list when it exists (valid), does not exists (invalid), and
    the list is empty (invalid).
    """
    task_list = TaskList()
    list_of_tasks = [Task("task 1"), Task("task 2"), Task("task 3")]
    valid_task = list_of_tasks[-1]
    valid_id = list_of_tasks[0].task_id
    invalid_task = Task("Not Added")
    invalid_id = invalid_task.task_id

    # Try to delete a task from an empty list (error state)
    with pytest.raises(TaskListError) as e:
        task_list.delete_task(valid_id)
    assert isinstance(e.value, EmptyTaskListError)

    with pytest.raises(TaskListError) as e:
        task_list.delete_task(invalid_id)
    assert isinstance(e.value, EmptyTaskListError)

    # Delete an existing task from the list by ID and by a `Task` object
    task_list = TaskList(task_list=list_of_tasks)
    task_list.delete_task(task=valid_id)
    task_list.delete_task(task=valid_task)

    # Try to get a task that does not exist in the list.
    with pytest.raises(TaskListError) as e:
        task_list.delete_task(invalid_id)
    assert isinstance(e.value, TaskNotFoundError)

    with pytest.raises(TaskListError) as e:
        task_list.delete_task(invalid_task)
    assert isinstance(e.value, TaskNotFoundError)

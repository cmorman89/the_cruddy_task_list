"""
TaskManager Module

The `TaskManager` class is responsible for abstracting and orchestrating calls to the data layer,
which includes the `Task` and `TaskList` classes. It provides the data operations available to the
user interface and service orchestration layers.

Classes:
    TaskManager: Responsible for abstracting the logic for and orchestrating the calls to the data
        in the application (such as `Task` and `TaskList` objects).
"""

from datetime import datetime
from typing import Any, Optional
from app.task import Task, TaskError
from app.task_list import TaskList, TaskListError, TaskNotFoundError


class TaskManager:
    """Responsible for abstracting the logic for and orchestrating the calls to the data in the
    application (such as `Task` and `TaskList` objects).

    Attributes:
        task_list (TaskList): The `TaskList`, which holds `Task` objects.

    Methods:
        set_task_title: Fetch a task and set its title.
        set_Task_description: Fetch a task and set its description.
        set_task_due_date: Fetch a task and set its due date.
        set_task_status: Fetch a task and set its status.
        get_task: Fetch a task from a task list based on a flexible identifier.
        get_task_by_id: Fetch a task from a task list based on its `task_id`
        get_task_by_index: Fetch a task from a task list based on its index value within the list.
        add_task_to_list: Add a unique task to the task list.
        delete_task_from_list: Remove an existing task from the task list.
    """

    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def _update_task_attribute(
        self, identifier: Task | str | int, attribute: str, value: Any
    ):
        """Fetch a task and attempt to set a provided attribute.

        Args:
            identifier (Task | str | int): The means of choosing the task to modify.
            attribute (str): The name of the attribute to modify.
            value (Any): The new value of the attribute
        """
        try:
            setattr(self.get_task(identifier), attribute, value)
        except TaskNotFoundError:
            print(
                f"Task not found when setting {attribute}={value} for identifier: {identifier}"
            )
        except TaskError as exc:
            print(f"{exc.value}")

    def set_task_title(self, identifier: Task | str | int, new_title: str):
        "Use the `_update_task_attribute` method to update the task's title"
        self._update_task_attribute(identifier, "title", new_title)

    def set_task_description(self, identifier: Task | str | int, new_desc: str):
        "Use the `_update_task_attribute` method to update the task's description"
        self._update_task_attribute(identifier, "description", new_desc)

    def set_task_due_date(
        self, identifier: Task | str | int, new_due_date: str | datetime
    ):
        "Use the `_update_task_attribute` method to update the task's due date"
        self._update_task_attribute(identifier, "due_date", new_due_date)

    def set_task_status(self, identifier: Task | str | int, new_status: str):
        "Use the `_update_task_attribute` method to update the task's status"
        self._update_task_attribute(identifier, "status", new_status)

    def get_task(self, identifier: Task | str | int) -> Task:
        """Fetch a task based on the provided identifier.

        Args:
            identifier (Task | str | int): The identifier for the task, which can be a Task object,
                a task ID (str), or an index (int).

        Returns:
            Task: The matching task object if found.

        Raises:
            TaskNotFoundError: If the task is not found.
        """
        if isinstance(identifier, Task):
            return identifier
        elif isinstance(identifier, str):
            return self.get_task_by_id(identifier)
        elif isinstance(identifier, int):
            return self.get_task_by_index(identifier)
        else:
            raise TaskNotFoundError("Invalid task identifier provided.")

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """Fetch a task from a task list based on the task's `task_id` attribute

        Args:
            task_id (str): The tasks `task_id` to match.

        Returns:
            Optional[Task]: Return a `Task` object if found.
        """
        try:
            return self.task_list.get_task(task_id=task_id)
        except TaskListError as exc:
            print(f"{exc.value}")
            return None

    def get_task_by_index(self, task_index: int) -> Optional[Task]:
        """Fetch a task from a task list based on the task's index location in the list.

        Args:
            task_index (int): The index of the task in the task list.

        Returns:
            Optional[Task]: Return a `Task` object if found.
        """
        try:
            return self.task_list.get_all_tasks()[task_index]
        except IndexError as exc:
            print(f"{exc.value}")
            return None

    def add_task_to_list(self, task: Task):
        """Add a unique task to the task list.

        Args:
            task (Task): The task to add.
        """
        try:
            self.task_list.add_task(task)
        except TaskListError as exc:
            print(f"{exc.value}")

    def delete_task_from_list(self, task: Task):
        """Delete an existing task from the task list.

        Args:
            task (Task): The task to delete.
        """
        try:
            self.task_list.delete_task(task)
        except TaskListError as exc:
            print(f"{exc.value}")

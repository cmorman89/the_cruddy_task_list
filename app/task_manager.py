"""
Task Manager Module

Responsible for CRUD operations required to create and manage list of `Task` objects.

Classes:
    TaskManager: Handle CRUD operations for `Task` objects and keep a list of tasks.
    TaskManagerError(Exception): Base exception for Task Manager errors.
    EmptyTaskListerror(TaskManagerError): Raise when trying to perform operations on an empty task
        list.
    TaskNotFoundError(TaskManagerError): Raise when a specific task is not found in the task list.
    AddDuplicateTaskError(TaskManagerError): Raise when trying to add a task already present in the
        task list.
"""

from typing import Optional, List

from app.task import Task


class TaskManagerError(Exception):
    """Base exception for Task Manager errors."""


class EmptyTaskListError(TaskManagerError):
    """Raise when trying to perform operations on an empty task list."""

    def __init__(self, method_name: Optional[str] = None):
        formatted_method_name = f" {method_name}" if method_name else '"'
        super().__init__(
            f"Cannot perform operation{formatted_method_name}. Task list is empty."
        )
        self.operation = method_name


class TaskNotFoundError(TaskManagerError):
    """Raise when a specific task is not found in the task list."""

    def __init__(self, task_id: int):
        super().__init__(f"No task found with task ID {task_id}.")
        self.task_id = task_id


class AddDuplicateTaskError(TaskManagerError):
    """Raise when trying to add a task already present in the task list."""

    def __init__(self, task: str):
        super().__init__(
            "Duplicate task already exists in the task list."
            + f' The "{task.title}" task was not added.'
        )
        self.task_title = task.title


class TaskManager:
    """Handle CRUD operations for `Task` objects and keep a list of tasks.

    Attributes:
        task_list (List[Task]): A list of `Task` objects that belong to this `TaskManager`

    Methods:
        add_task: Add a `Task` obj to the list if is not already in the list.
        get_task: Return the `Task` obj in the list with the matching `task_id`.
        delete_task: Remove a `Task` obj from the task list if it is present.
    """

    def __init__(self, task_list: Optional[List[Task]] = None):
        """Construct the `TaskManager` object with a task list.

        Args:
            task_list (Optional[List[Task]], optional): The lists of tasks held by this
                `TaskManager`. Defaults to None.
        """
        self.task_list: List[Task] = task_list if task_list else []

    def add_task(self, task: Task):
        """Adds a `Task` to the task list if it is not a duplicate.

        Args:
            task (Task): The new `Task` to add to the task list.

        Raises:
            AddDuplicateTaskError: if attempting to add a task that is already in the task list.
        """
        if task not in self.task_list:
            self.task_list.append(task)
        else:
            raise AddDuplicateTaskError(task)

    def get_task(self, task_id: int) -> Optional[Task]:
        """Fetch a `Task` object from the task list using its unique `task_id` value.

        Args:
            task_id (int): The `task_id` of the `Task` object to locate.

        Raises:
            EmptyTaskListError: if the task_list is empty.
            TaskNotFoundError: if a `Task` with a matching `task_id` value is not found in the
                task manager's list.

        Returns:
            Optional[Task]: The matching `Task` object.
        """
        if self.task_list:
            try:
                return next(task for task in self.task_list if task.task_id == task_id)
            except StopIteration as e:
                raise TaskNotFoundError(task_id) from e
        raise EmptyTaskListError(method_name="get_task()")

    def get_all_tasks(self) -> List[Optional[Task]]:
        """Fetch the complete lists of tasks from the task list.

        Returns:
            List[Task]: The list of 'Task' objects.
        """
        return self.task_list

    def delete_task(self, task_id: int):
        """Delete a `Task` from the task list if it is present.

        Args:
            task_id (int): The `task_id` of the `Task` object to locate and remove.

        Raises:
            EmptyTaskListError: if the task_list is empty.
            TaskNotFoundError: if a `Task` with a matching `task_id` value is not found in the
                task manager's list.
        """
        if self.task_list:
            task = self.get_task(task_id=task_id)
            self.task_list.remove(task)
        else:
            raise EmptyTaskListError(method_name="`delete_task()`")

    def __str__(self):
        """Produces a simple, printable task list."""
        repr = "Task List:\n"
        if self.task_list:
            for i, task in enumerate(self.get_all_tasks()):
                repr += f"  {i + 1}.\t{task.title}  (ID#{task.task_id})\n"
        else:
            repr += "  - No tasks in the task list.\n"

        return repr

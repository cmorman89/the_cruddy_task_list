"""
Task Module:

This module represents a task and defines the attributes it can have. Ensures each `Task`
object has a unique ID number by using the utility class `TaskID` and its `generate()` method.

Classes:
    Task: Responsible for holding task-related information such as an ID, title, due date, etc.
    TaskError: Base `Exception` for all `Task`-related errors.
    BlankTitleError: Raise when attempting ot set a title to None or a blank/empty string.
"""

from typing import Optional, List
from datetime import datetime

from app.task_id import TaskID


class TaskError(Exception):
    """Base Exception for all Task-related errors."""


class BlankTitleError(TaskError):
    """Raise when attempting to set a title to None or a blank/empty string.

    Attributes:
        task_id (int): The ID of the task that raised the exception.
    """

    def __init__(self, task_id: int):
        super().__init__("Task name cannot be blank for task ID #{task_id}.")
        self.task_id = task_id

class Task:
    """Responsible for holding task-related information such as an ID, title, due date, etc.

    Attributes:
        task_id (int): The unique ID of the task, automatically generated using
            `TaskID.generate()` during instantiation. Immutable once set.
        title (str): A short title or description of the task.
        description (Optional[str], optional): A longer description of the task details. Defaults
            to None.
        status (str): The current status of the task. Must be set as "Pending", "In Progress", or
            "Completed". Defaults to "Pending".
        due_date (Optional[datetime], optional): The due date of the task. Defaults to the current
            date/time.

    Methods:
        _validate_status: Validate the status field to ensure it is one of the allowed status
            options.
    """

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        status: Optional[str] = "Pending",
    ):
        """Construct a task with requested args and ensures it has a valid ID, status, and due
        date.

        Args:
            title (str): A short title or description of the task.
            description (Optional[str], optional): A longer description of the task details.
                Defaults to None.
            due_date (Optional[datetime], optional): The due date of the task. Defaults to None.
            status (str): The current status of the task. Must be set as "Pending", "In Progress",
                or "Completed". Defaults to "Pending".
        """
        self._task_id: int = TaskID.generate()
        self.title: str = title
        self.description: Optional[str] = description
        self.due_date: datetime = due_date if due_date else datetime.now()
        self.status: str = status

    @property
    def task_id(self) -> int:
        """Safely return the `_task_id` attribute while ensuring immutability.

        Returns:
            int: The ID number of this task.
        """
        return self._task_id

    @property
    def title(self) -> str:
        """Return the title of the task."""
        return self._title

    @title.setter
    def title(self, new_title: str):
        """Set the title of the task to a valid, non-empty string.

        Args:
            new_title (str): The new title of the task

        Raises:
            BlankTitleError: If `None` or a blank/empty string is passed.
        """
        if new_title is None or new_title.strip() == "":
            raise BlankTitleError(task_id=self.task_id)
        else:
            self._title = new_title

    @property
    def status(self) -> str:
        """Gets the task's status.

        Returns:
            str: The task's status.
        """
        return self._status

    @status.setter
    def status(self, new_status: str):
        """Set the task status if valid, or prints an error and sets as "Pending" if invalid.

        Args:
            new_status (str): The unvalidated new status for the task.
        """
        try:
            self._status = self._validate_status(new_status)
        except ValueError as status_error:
            print(f"{status_error}")
            self._status = "Pending"

    @staticmethod
    def _validate_status(new_status: str) -> str:
        """Validate the status field to ensure it is one of the allowed status options.

        Args:
            new_status (str): The new status to validate and return.

        Raises:
            ValueError: If the `new_status` is not in `valid_statuses`.

        Returns:
            str: The validated task status.
        """
        valid_statuses = ["Pending", "In Progress", "Completed"]
        new_status = "(empty)" if not new_status else new_status
        if new_status.lower() in map(str.lower, valid_statuses):
            return next(
                status
                for status in valid_statuses
                if status.lower() == new_status.lower()
            )
        else:
            raise ValueError(
                f"Unable to set status to {new_status}. Valid options are {valid_statuses}."
            )

    def __str__(self):
        """Return a user-friendly string representation of the task.

        The string includes the task's title and ID in the format:
            "<title> (ID #<task_id>)".

        Returns:
            str: A readable representation of the task.
        """
        return f"{self.title} (ID #{self.task_id})"

    def __repr__(self):
        """Return a string representation of the task with a complete list of its attributes.

        The string includes the complete task attributes in the format:
            <Task: task_id="<task_id>", title="<task_title>", description="<description>",
            due_date=<due_date>, status="<status>">

        Returns:
            str: A complete representation of the task.
        """
        return (
            f'<Task: task_id="{self.task_id}", '
            f'title="{self.title}", '
            f'description="{self.description}", '
            f"due_date={self.due_date.strftime("%Y-%m-%d %H:%M")}, "
            f'status="{self.status}">'
        )

"""
Task Module:

This module represents a task and defines the attributes it can have. Ensures each `Task`
object has a unique ID number by using the utility class `TaskID` and its `generate()` method.

Classes:
    Task: Responsible for holding task-related information such as an ID, title, due date, etc.
    TaskError: Base `Exception` for all `Task`-related errors.
    BlankTitleError: Raise when attempting ot set a title to None or a blank/empty string.
    InvalidStatusError: Raise when attempting to set a status that is not in the list of valid
        statues.
"""

from typing import Optional, List
from datetime import datetime

from app.task_id import TaskID


class TaskError(Exception):
    """Base Exception for all Task-related errors."""


class InvalidTaskTitleError(TaskError):
    """Raise when attempting to set a title to None or a blank/empty string.

    Attributes:
        task_id (int): The ID of the task that raised the exception.
    """

    def __init__(self, task_id: int):
        super().__init__(f"Task name cannot be blank for task ID #{task_id}.")
        self.task_id = task_id


class InvalidTaskStatusError(TaskError):
    """Raise when attempting to set a status that is not in the list of valid statuses.

    Attributes:
        task_id (int): The ID of the task that raised the exception.
        attempted_status (str): The invalid status attempted by the user.
        valid_statuses List[str]: The list of valid statuses that may be set.
    """

    def __init__(self, task_id: int, attempted_status: str, valid_statuses: List[str]):
        super().__init__(
            f'Unable to set status to "{attempted_status}" for task ID #{task_id}. '
            f"Valid options are {valid_statuses}."
        )
        self.attempted_status = attempted_status
        self.valid_statuses = valid_statuses


class Task:
    """Responsible for holding task-related information such as an ID, title, due date, etc.

    Attributes:
        VALID_STATUSES (List[str]): A complete list of valid `status` strings.
        task_id (int): The unique ID of the task, automatically generated using
            `TaskID.generate()` during instantiation. Immutable once set.
        title (str): A short title or description of the task. Must not be blank or `None`.
        description (Optional[str], optional): A longer description of the task details. Defaults
            to `None`.
        status (str): The current status of the task. Must be set as "Pending", "In Progress", or
            "Completed". Defaults to "Pending".
        due_date (Optional[datetime], optional): The due date of the task. Defaults to the current
            date/time.
    """

    VALID_STATUSES = ["pending", "in progress", "completed"]

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        status: Optional[str] = "pending",
    ):
        """Construct a task with requested args and ensures it has a valid ID, status, and due
        date.

        Args:
            title (str): A short title or description of the task. Must not be blank or `None.
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
        """Validates and then sets the task's title.

        Args:
            new_title (str): The new title of the task

        Raises:
            TaskTitleError: If the title fails validation before being set.
        """
        if not self.validate_title(new_title=new_title):
            raise InvalidTaskTitleError(self.task_id)
        self._title = new_title

    @staticmethod
    def validate_title(new_title: str) -> bool:
        """Validate that the title is meaningful.

         A meaningful title must be a non-empty string with at least one printable
         character.

        Args:
            new_title (str): The new title to validate.

        Returns:
            bool: `True` if valid; `False` if invalid.
        """
        return True if isinstance(new_title, str) and new_title.strip() else False

    @property
    def status(self) -> str:
        """Gets the task's status.

        Returns:
            str: The task's status.
        """
        return self._status

    @status.setter
    def status(self, new_status: str):
        """Validates and sets the `status` attribute.

        Args:
            new_status (str): The new status to validate and set.

        Raises:
            InvalidTaskStatusError: If the `new_status` is not in `valid_statuses`.
        """
        if not self.validate_status(new_status=new_status):
            raise InvalidTaskStatusError(self.task_id, new_status, Task.VALID_STATUSES)
        self._status = new_status.lower()

    @staticmethod
    def validate_status(new_status: str):
        return (
            True
            if isinstance(new_status, str) and new_status.lower() in Task.VALID_STATUSES
            else False
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

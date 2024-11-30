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

from typing import Optional
from datetime import datetime

from app.task_id import TaskID
from app.task_validator import TaskValidator


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
    """

    def __init__(self, task_id: int, attempted_status: str):
        valid_statuses = TaskValidator.VALID_STATUSES
        super().__init__(
            f'Unable to set status to "{attempted_status}" for task ID #{task_id}. '
            f"Valid options are {valid_statuses}."
        )
        self.attempted_status = attempted_status
        self.valid_statuses = valid_statuses


class InvalidTaskDueDateError(TaskError):
    """Raise when attempting to set a due date to an unparsable string or non-`datetime` object.

    Attributes:
        new_due_date (str | datetime): The due date user input that failed validation
    """

    def __init__(self, task_id: int, new_due_date: str | datetime):
        super().__init__(f'Invalid date "{new_due_date}" for task ID #{task_id}.')
        self.new_due_date = new_due_date


class Task:
    """Responsible for holding task-related information such as an ID, title, due date, etc.

    Attributes:
        task_id (str): The unique ID of the task, automatically generated using
            `TaskID.generate()` during instantiation. Immutable once set.
        title (str): A short title or description of the task. Must not be blank or `None`.
        description (Optional[str], optional): A longer description of the task details. Defaults
            to `None`.
        status (str): The current status of the task. Must be set as "pending", "in progress", or
            "completed". Defaults to "pending".
        due_date (Optional[datetime], optional): The due date of the task. Defaults to the current
            date/time.
    """

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
            status (str): The current status of the task. Must be set as "pending", "in progress",
            or "completed". Defaults to "pending".
        """
        self._task_id: str = TaskID.generate()
        self._title: str
        self._due_date: datetime
        self._status: str

        self.title = title
        self.description: Optional[str] = description
        self.due_date = due_date if due_date else datetime.now()
        self.status = status if status else "pending"

    @property
    def task_id(self) -> str:
        """Safely return the `_task_id` attribute while ensuring immutability.

        Returns:
            str: The ID number of this task.
        """
        return self._task_id

    @property
    def title(self) -> str:
        """Return the title of the task.

        Returns:
            str: The task's title.
        """
        return self._title

    @title.setter
    def title(self, new_title: str):
        """Validate and then set the task's title.

        Args:
            new_title (str): The new title of the task

        Raises:
            TaskTitleError: If the title fails validation before being set.
        """
        if not TaskValidator.validate_title(new_title=new_title):
            raise InvalidTaskTitleError(self.task_id)
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
        """Validates and sets the task's status.

        Args:
            new_status (str): The new status to validate and set.

        Raises:
            InvalidTaskStatusError: If the new status fails validation before being set.
        """
        if not TaskValidator.validate_status(new_status=new_status):
            raise InvalidTaskStatusError(self.task_id, new_status)
        self._status = new_status.lower()

    @property
    def due_date(self) -> datetime:
        """Gets the task's due date.

        Returns:
            datetime: The task's due date.
        """
        return self._due_date

    @due_date.setter
    def due_date(self, new_due_date: str | datetime):
        """Validates and sets the task's due date.

        Args:
            new_due_date (datetime): The new status to validate and set.

        Raises:
            InvalidTaskDueDateError: If the new due date fails validation before being set.
        """
        if not TaskValidator.validate_due_date(new_due_date=new_due_date):
            raise InvalidTaskDueDateError(self.task_id, str(new_due_date))
        self._due_date = (
            new_due_date
            if isinstance(new_due_date, datetime)
            else datetime.strptime(new_due_date, "%m/%d/%Y")
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

    def __eq__(self, other):
        """Check if another object is equal to this Task's id or title if a string. If it is another
        `Task`, check if both `task_id` match.
        """
        if isinstance(other, str):
            return other == self.task_id or other == self.title
        elif isinstance(other, Task):
            return other.task_id == self.task_id
        return False

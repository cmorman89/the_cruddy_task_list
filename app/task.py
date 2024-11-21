"""
Task Module:

This module represents a task and defines the attributes it can have. Ensures each `Task`
object has a unique ID number by using the utility class `TaskID` and its `generate()` method.

Classes:
    Task: Responsible for holding task-related information such as an ID, title, due date, etc.
"""

from typing import Optional
from datetime import datetime

from app.task_id import TaskID


class Task:
    """Responsible for holding task-related information such as an ID, title, due date, etc.

    Attributes:
        _task_id (int): The unique ID of the task, automatically generated using
            `TaskID.generate()`.
        title (str): A short title or description of the task.
        description (Optional[str], optional): A longer description of the task details. Defaults
            to None.
        status (str): The current status of the task. Must be set as "Pending", "In Progress", or
            "Completed". Defaults to "Pending".
        due_date (Optional[datetime], optional): The due date of the task. Defaults to the current
            date/time.
    """

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        status: Optional[str] = None,
    ):
        """Constructs a task with requested args and ensures it has a valid ID, status, and due
        date.

        Args:
            title (str): A short title or description of the task.
            description (Optional[str], optional): A longer description of the task details.
                Defaults to None.
            due_date (Optional[datetime], optional): The due date of the task. Defaults to None.
        status (str): The current status of the task. Must be set as "Pending", "In Progress", or
            "Completed". Defaults to None.
        """
        self._task_id = TaskID.generate()
        self.title = title
        self.description = description
        self.status = status if status else "Pending"
        self.due_date = due_date if due_date else datetime.now()

    @property
    def task_id(self) -> int:
        """Safely return the `_task_id` attribute while ensuring immutability.

        Returns:
            int: The ID number of this task.
        """
        return self._task_id

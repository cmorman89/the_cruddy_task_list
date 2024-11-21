"""
Task Module:

This module represents a task and defines the attributes it can have.

Classes:
    Task: Responsible for holding task-related information such as an ID, title, due date, etc.
"""

from typing import Optional
from datetime import datetime


class Task:
    """Responsible for holding task-related information such as an ID, title, due date, etc.

    Attributes:
        next_task_id: Class attribute that tracks the next available `task_id` to ensure uniqueness across instances.
        _task_id (int): The unique ID of the task, automatically generated using `Task.next_task_id`.
        title (str): A short title or description of the task.
        description (Optional[str], optional): A longer description of the task details. Defaults to None.
        status (str): The current status of the task. Must be "Pending", "In Progress", or "Completed". Defaults to "Pending".
        due_date (Optional[datetime], optional): The due date of the task. Defaults to current date/time.
    """

    next_task_id: int = 0

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
        status: Optional[str] = None,
    ):
        """Constructs a basic Task.

        Args:
            title (str): A short title or description of the task.
            description (Optional[str], optional): A longer description of the task details. Defaults to None.
            due_date (Optional[datetime], optional): The due date of the task. Defaults to None.
            status (Optional[str], optional): The current status of the task. Can be "Pending", "In Progress", or "Completed".
        """
        self._task_id = Task.next_task_id
        self.title = title
        self.description = description
        self.status = "Pending"
        self.due_date = due_date if due_date else datetime.now()

"""
Task Module
"""

from typing import Optional
from datetime import datetime


class Task:

    next_task_id: int = 0

    def __init__(
        self,
        title: str,
        description: Optional[str] = None,
        due_date: Optional[datetime] = None,
    ):
        """Constructs a basic Task.

        Args:
            title (str): _description_
            description (Optional[str], optional): _description_. Defaults to None.
            due_date (Optional[datetime], optional): _description_. Defaults to None.
        """
        self._task_id = Task.next_task_id
        self.title = title
        self.description = description
        self.status = "Pending"
        self.due_date = due_date if due_date else datetime.now()

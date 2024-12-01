from datetime import datetime
from typing import Optional
from app.task import Task, TaskError
from app.task_list import TaskList, TaskListError, TaskNotFoundError


class TaskManager:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def _update_task_attribute(
        self, identifier: Task | str | int, attribute: str, value
    ):
        try:
            setattr(self.get_task(identifier), attribute, value)
        except TaskNotFoundError:
            print(
                f"Task not found when setting {attribute}={value} for identifier: {identifier}"
            )
        except TaskError as exc:
            print(f"{exc.value}")

    def set_task_title(self, identifier: Task | str | int, new_title: str):
        self._update_task_attribute(identifier, "title", new_title)

    def set_task_description(self, identifier: Task | str | int, new_desc: str):
        self._update_task_attribute(identifier, "description", new_desc)

    def set_task_due_date(
        self, identifier: Task | str | int, new_due_date: str | datetime
    ):
        self._update_task_attribute(identifier, "due_date", new_due_date)

    def set_task_status(self, identifier: Task | str | int, new_status: str):
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

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        try:
            return self.task_list.get_task(task_id=task_id)
        except TaskListError as exc:
            print(f"{exc.value}")
            return None

    def get_task_by_index(self, task_index: int) -> Optional[Task]:
        try:
            return self.task_list.get_all_tasks()[task_index]
        except IndexError as exc:
            print(f"{exc.value}")
            return None

    def add_task_to_list(self, task: Task):
        try:
            self.task_list.add_task(task)
        except TaskListError as exc:
            print(f"{exc.value}")

    def delete_from_list(self, task: Task):
        try:
            self.task_list.delete_task(task)
        except TaskListError as exc:
            print(f"{exc.value}")

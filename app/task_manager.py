"""
Task Manager Module

Responsible for CRUD operations required to create and manage list of `Task` objects.

Classes:
    TaskManager: Handle CRUD operations for `Task` objects and keep a list of tasks.
    TaskManagerError(Exception): Base exception for Task Manager errors.
    EmptyTaskListError(TaskManagerError): Raise when trying to perform operations on an empty task
        list.
    TaskNotFoundError(TaskManagerError): Raise when a specific task is not found in the task list.
    AddDuplicateTaskError(TaskManagerError): Raise when trying to add a task already present in the
        task list.
"""

from typing import Optional, List, Union

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
        get_all_tasks: Return the entire task list.
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

    def get_task(self, task_id: int) -> Task:
        """Fetch a `Task` object from the task list using its unique `task_id` value.

        Args:
            task_id (int): The `task_id` of the `Task` object to locate.

        Raises:
            EmptyTaskListError: if the task_list is empty.
            TaskNotFoundError: if a `Task` with a matching `task_id` value is not found in the
                task manager's list.

        Returns:
            Task: The matching `Task` object.
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

    def delete_task(self, task: Union[int, Task]):
        """Delete a `Task` from the task list if it is present.

        Args:
            task (Union[int, Task]): Either the `task_id` of the `Task` to locate and remove
                                    or the `Task` object itself.

        Raises:
            EmptyTaskListError: if the task_list is empty.
            TaskNotFoundError: if a `Task` with a matching `task_id` value is not found in the
                task manager's list.
        """
        task_id = task if isinstance(task, int) else task.task_id
        if self.task_list:
            task = self.get_task(task_id=task_id)
            self.task_list.remove(task)
        else:
            raise EmptyTaskListError(method_name=f"`delete_task()` for `task_id` == {task_id}")

    def __str__(self):
        """Return a user-friendly string representation of the task.

        The string includes task position in the list, the task titles, and their task_ids in the
        following format:
            Task List:
            1.    <Task string>
            2.    <Task string>
            3.    ...

        An empty list returns :
            Task List:
            - No tasks in the task list.

        Returns:
            str: A brief representation of the task manager/task list.
        """
        list_str = "Task List:\n"
        if self.task_list:
            for i, task in enumerate(self.get_all_tasks()):
                list_str += f"  {i + 1}.\t{task}\n"
        else:
            list_str += "  - No tasks in the task list.\n"
        return list_str

    def __repr__(self):
        """Return a string representation of all tasks and their attributes present in the list.

        The string includes the complete task list and child task attributes in the format:
            <TaskManager: task_list=[<Task: ...>, <Task: ...>]>

        Returns:
            str: A complete representation of the task manager/task list.
        """
        task_list = []
        for task in self.get_all_tasks():
            task_list.append(f"{task!r}")
        return f"<TaskManager: task_list={task_list}>"

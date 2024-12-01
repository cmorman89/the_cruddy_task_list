"""
Task ID Generator Utility Module

Manages and provides a unique ID number for `Task` objects by keeping an internal counter of the
last issued ID number, and incrementing it before providing it to the next `Task` object.

Classes:
    TaskID: Manages and provides a unique ID number for `Task` objects.
"""


class TaskID:
    """Manages and provides a unique ID number as a string for `Task` objects

    Attributes:
        _last_task_id (int): The internal counter for tracking issued IDs.

    Methods:
        generate: Generates and returns a unique ID.
    """

    _last_task_id: int = -1

    @staticmethod
    def generate() -> str:
        """Generates a unique ID by incrementing the `_last_task_id` counter.

        Returns:
            str: The unique ID as a string.
        """
        TaskID._last_task_id += 1
        return str(TaskID._last_task_id)

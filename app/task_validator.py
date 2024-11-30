"""
Task Validator Class

Provides a centralized location for the validation logic needed when setting task attributes. They
are all static methods and all return `True` if the input is valid, or `False` if it is invalid.
This allows any part of the program to access validation logic without having to directly interface
with the `Task` class or having to instantiate any validation-type object to perform the checks.

Classes:
    TaskValidator: Defines the static methods to validate a given input for correctness for each of
        the `Task` object's attributes.
"""

import re
from datetime import datetime


class TaskValidator:
    """Provides the static methods and overall logic to validate a given input for correctness in
        relation to any of the `Task` class' attributes. All methods return `True` if the input is
        valid, or `False` if it is invalid.

    Attributes:
        VALID_STATUSES (List[str]): A complete list of valid `status` strings.

    Methods:
        validate_title: Check if the new string is not blank or empty.
        validate_description: Check if the new description is a string or `None`.
        validate_status: Check if the new status string is present in a list of valid statues.
        validate_due_date: Check if the new due date is a `datetime` obj or a string (_M/_D/YYYY)
    """

    VALID_STATUSES = ["pending", "in progress", "completed"]

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

    @staticmethod
    def validate_description(new_desc: str):
        """Validate the description of a task.

        As it is optional, any string or `None` is valid.

        Args:
            new_desc (str): _description_

        Returns:
            _type_: _description_
        """
        return True if new_desc is None or isinstance(new_desc, str) else False

    @staticmethod
    def validate_status(new_status: str):
        """Validate that the status is one of the predefined strings in Task.VALID_STATUSES

        Args:
            new_status (str): The new status to validate.

        Returns:
            bool: `True` if valid; `False` if invalid.
        """
        return (
            True
            if isinstance(new_status, str)
            and new_status.lower() in TaskValidator.VALID_STATUSES
            else False
        )

    @staticmethod
    def validate_due_date(new_due_date: str | datetime):
        """Validate that the due date is a `datetime` object or a formatted string.

        The string format is _M/_D/YYYY with/without leading zeroes. Year must be all four digits.

        Args:
            new_status (str): The new status to validate.

        Returns:
            bool: `True` if valid; `False` if invalid.

        Note:
            Use `elif` to match more regex patterns.
        """

        if isinstance(new_due_date, datetime):
            return True
        elif isinstance(new_due_date, str) and re.match(
            r"\d{1,2}\/\d{1,2}\/\d{4}", new_due_date
        ):
            try:
                datetime.strptime(new_due_date, "%m/%d/%Y")
                return True
            except ValueError:
                return False
        return False

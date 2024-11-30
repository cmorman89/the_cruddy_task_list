"""
Test the `task_validator.py` module
"""

from datetime import datetime
import pytest

from app.task_validator import TaskValidator


def test_valid_statuses():
    """Test that `VALID_STATUSES` list exists and is populated with strings."""
    assert isinstance(TaskValidator.VALID_STATUSES, list)
    for status in TaskValidator.VALID_STATUSES:
        assert isinstance(status, str)


@pytest.mark.parametrize(
    "title, valid",
    [
        # Valid
        ("Complete project report", True),
        ("Buy groceries", True),
        ("Meeting with team at 10 AM", True),
        ("Fix bug #123", True),
        ("Call John about contract renewal", True),
        ("Prepare presentation slides", True),
        ("Book dentist appointment", True),
        ("Submit timesheet", True),
        ("Research new marketing strategies", True),
        ("Organize workspace", True),
        # Invalid
        ("", False),
        ("   ", False),
        (None, False),
        ("\t\n", False),
        ("   \n", False),
        (" ", False),
    ],
)
def test_validate_title(title, valid):
    """Test valid and invalid titles to ensure validation is correct.

    Args:
        title (str): The title to test.
        valid (bool): The expected validator output.
    """
    assert TaskValidator.validate_title(new_title=title) == valid


@pytest.mark.parametrize(
    "description, valid",
    [
        # Valid
        ("Complete the project documentation", True),
        ("Buy groceries and household supplies", True),
        ("Schedule a team meeting for next week", True),
        ("Fix bug #123 in the codebase", True),
        ("Prepare slides for the upcoming presentation", True),
        ("", True),
        (None, True),
        (" ", True),
        ("\nWrite unit tests for new feature\n", True),
        ("Follow up with client on feedback", True),
        # Invalid
        #  - No invalid examples.
    ],
)
def test_validate_description(description, valid):
    """Test valid descriptions to ensure validation is correct. Since all descriptions are valid,
    this mainly checks nothing has broken the basic functionality.

    Args:
        title (str): The title to test.
        valid (bool): The expected validator output.
    """
    assert TaskValidator.validate_description(new_desc=description) == valid


@pytest.mark.parametrize(
    "status, valid",
    [
        # Valid
        ("pending", True),
        ("in progress", True),
        ("completed", True),
        ("Pending", True),
        ("IN PROGRESS", True),
        # Invalid
        ("done", False),
        ("started", False),
        ("not started", False),
        ("waiting", False),
        ("finished", False),
        ("", False),
        (" ", False),
        (None, False),
        ("complete", False),
        ("inprogress", False),
    ],
)
def test_validate_status(status, valid):
    """Test valid and invalid statuses to ensure validation is correct.

    Args:
        status (str): The status to test.
        valid (bool): The expected validator output.
    """
    assert TaskValidator.validate_status(new_status=status) == valid


@pytest.mark.parametrize(
    "due_date, valid",
    [
        # Valid
        ("01/01/2024", True),
        ("12/31/2024", True),
        ("3/15/2025", True),
        ("07/04/2024", True),
        ("7/4/2024", True),
        ("11/11/2024", True),
        (datetime(2024, 1, 1), True),
        (datetime(2025, 12, 31), True),
        (datetime(2023, 6, 10), True),
        (datetime(2024, 11, 25), True),
        (datetime(2024, 5, 20), True),
        # Invalid
        ("2024-01-01", False),
        ("January 1, 2024", False),
        ("1/1/24", False),
        ("2024/01/01", False),
        ("01-01-2024", False),
        ("13/01/2024", False),
        ("02/30/2024", False),
        ("02/01/24", False),
        (" ", False),
        ("", False),
        (None, False),
    ],
)
def test_validate_due_date(due_date, valid):
    """Test valid and invalid due dates (string and `datetime`) to ensure validation is correct.

    Args:
        due_date (str | datetime): The due_date to test.
        valid (bool): The expected validator output.
    """
    assert TaskValidator.validate_due_date(new_due_date=due_date) == valid

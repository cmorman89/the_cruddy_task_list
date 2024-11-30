"""
Test the `task_validator.py` module
"""

import pytest

from app.task_validator import TaskValidator


@pytest.mark.parametrize(
    "title, valid",
    [
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
        ("", False),
        ("   ", False),
        (None, False),
        ("\t\n", False),
        ("   \n", False),
        (" ", False),
    ],
)
def test_validate_title(title, valid):
    assert TaskValidator.validate_title(new_title=title) == valid

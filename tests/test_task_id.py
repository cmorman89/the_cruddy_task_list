"""
Tests for the `TaskID` Module
"""

from app.task_id import TaskID


def test_id_generation():
    """Generates a list of IDs and checks if they are unqiue by converting to set and comparing
    the length before and after"""
    id_list = [TaskID.generate() for id in range(100)]
    assert len(id_list) == len(set(id_list))

"""
A C.R.U.D.dy To-Do List

"""

from app.task import Task
from app.task_manager import TaskManager

if __name__ == "__main__":

    task_manager = TaskManager()
    task = Task("title")
    task1 = Task("title1")
    task2 = Task("title2")
    task3 = Task("title3")
    task_manager.add_task(task)
    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)
    print(task_manager)

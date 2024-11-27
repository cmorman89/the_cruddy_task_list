"""
A C.R.U.D.dy To-Do List

"""

from app.task import Task
from app.task_list import TaskList

if __name__ == "__main__":

    task_list = TaskList()
    print(task_list)
    print(f"{task_list!r}")
    task = Task("title")
    task1 = Task("title1")
    task2 = Task("title2")
    task3 = Task("title3")
    task_list.add_task(task)
    task_list.add_task(task1)
    task_list.add_task(task2)
    task_list.add_task(task3)
    print(task_list)
    print(f"{task_list!r}")

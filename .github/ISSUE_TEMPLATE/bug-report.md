---
name: Bug Report
about: Report a bug or issue with the project
title: "[BUG] Short description of the bug \U0001F41B"
labels: bug
assignees: cmorman89

---

## 🐛 Bug Summary

### Description
<!-- Provide a clear and concise description of the bug -->

**Severity/Priority:** <!-- Select one -->
- **Critical** 🔴
- **High** 🟠
- **Medium** 🟡
- **Low** 🟢

**Status:** <!-- Select one -->
- **Accepted** 👍
- **In Progress** ⏳
- **On Hold** ⏸️
- **Pending Review** ❓
- **Closed, Resolved** ✅
- **Closed, Unresolved** 🚫

---

## Steps to Reproduce
<!-- Provide a list of steps to reproduce the bug -->

1. **Step 1:** <!-- e.g., Create a `TaskManager` with a list of duplicate tasks -->
    ```python
    # Example code to reproduce
    task = Task(name="Task 1")
    list_with_dupl = [task, task, task]
    task_manager = TaskManager(list_with_dupl)
    ```
2. **Step 2:** <!-- e.g., Observe that no error is raised and duplicates are stored -->

---

## Expected Behavior
<!-- Describe the expected behavior -->
The `TaskManager` should raise an exception if duplicate tasks are provided during initialization.

---

## Proposed Fix
<!-- Provide a proposed fix or solution -->

- Convert the task list to a `set` and compare lengths:
    ```python
    if len(task_list) != len(set(task_list)):
        raise DuplicateTaskError("Task list contains duplicates.")
    ```
- Add a unit test to ensure duplicate tasks during initialization raise an error.

---

## Impact
<!-- Describe the potential impact of this bug -->
Duplicate tasks can cause issues and unexpected behavior with lookup, ordering, and other operations like removal.

---

## Environment
<!-- Provide any relevant environment details -->
- **OS:** <!-- e.g., Windows 10 / macOS Monterey / Ubuntu 20.04 -->
- **Python Version:** <!-- e.g., Python 3.10 -->
- **Version of Project:** <!-- e.g., v0.1-alpha -->

---

**Additional Context**
<!-- Add any other context about the problem here -->

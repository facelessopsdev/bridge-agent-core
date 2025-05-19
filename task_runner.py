class TaskRunner:
    """Manage a list of tasks for Bridge Agent."""

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        """Add a task to the internal task list."""
        self._tasks.append(task)

    def list_tasks(self):
        """Print all stored tasks."""
        for task in self._tasks:
            print(task)

    def clear_tasks(self):
        """Remove all tasks from the internal list."""
        self._tasks = []

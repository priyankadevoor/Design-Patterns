"""
The task management system should allow users to create, update, and delete tasks.
Each task should have a title, description, due date, priority, and status (e.g., pending, in progress, completed).
Users should be able to assign tasks to other users and set reminders for tasks.
The system should support searching and filtering tasks based on various criteria (e.g., priority, due date, assigned user).
Users should be able to mark tasks as completed and view their task history.

create_user()
user should be able to create task
update task 
delete task
get all tasks with status
"""

"""
Enhancements - Search task based on keyword
Filter tasks based on status, assigned to and due date
"""
from User import User
from Task import Task
from TaskStatus import TaskStatus
from PriorityType import PriorityType

class TaskManager:
    def __init__(self):
        self._tasks = {}
        self._user_tasks = {}

    def create_task(self, task):
        self._tasks[task.get_taskid()] = task
        self._user_tasks[task.get_assigned_to().get_user_id()] = task

    def change_priority(self, task, priority_type):
        task.change_priority(priority_type)

    def change_status(self, task, status):
        task.change_status(status)

    def delete_task(self, task_id):
        task = self._tasks.pop(task_id, None)
        if task:
            user_id = task.get_assigned_to().get_user_id()
            del self._user_tasks[user_id]
    
    def print_tasks(self):
        print(self._tasks, self._user_tasks)

task_manager = TaskManager()
priya = User('Priya', 'priyadevoor@gmail.com')
shiv = User('Shivani', 'shivanidevoor@gmail.com')
task1 = Task('task1', 'Leetcode', 'Revise 3 BS Leetcode problems', TaskStatus.PENDING, PriorityType.LOW, '15-04-2025', priya)
task_manager.create_task(task1)
task_manager.change_priority(task1, PriorityType.HIGH)
print(task1.get_priority())
(task_manager.print_tasks())
task_manager.delete_task('task1')
(task_manager.print_tasks())




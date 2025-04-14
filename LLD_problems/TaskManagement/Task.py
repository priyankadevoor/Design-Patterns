class Task:
    def __init__(self, title, description, status, priority, due_date, assigned_to, assigned_by):
        self._title = title
        self._description = description
        self._status = status
        self._priority = priority
        self._due_date = due_date
        self._assigned_to = assigned_to
        self._assigned_by = assigned_by

    def get_title(self):
        return self._title
    
    def get_description(self):
        return self._description
    
    def get_task_status(self):
        return self._status
    
    def change_status(self, status):
        self._status = status
    
    def get_priority(self):
        return self._priority
    
    def change_priority(self, priority):
        self._priority = priority
    
    def get_due_date(self):
        return self._due_date
    
    def change_due_date(self, due_date):
        self._due_date = due_date

    def get_assigned_to(self):
        return self._assigned_to
    
    def get_assigned_by(self):
        return self._assigned_by

import datetime

class Task:
    def __init__(self, task):
        self._id = task[0]
        self._created_date = task[1]
        self._task = task[2]
        self._deadline = task[3]

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def created_date(self) -> datetime.date:
        return self._created_date
    
    @property
    def task(self) -> str:
        return self._task
    
    @property
    def deadline(self) -> datetime.date:
        return self._deadline

    def __str__(self) -> str:
        if self.deadline < datetime.date.today():
            return '\033[31m' + 'Task {}(OVERDUE): {}.\ndeadline: {}'.format(self.id, self.task, self.deadline) + '\033[0m'
        elif self.deadline == datetime.date.today():
            return '\033[33m' + 'Task {}: {}.\ndeadline: {}'.format(self.id, self.task, self.deadline) + '\033[0m'
        else:
            return '\033[32m' + 'Task {}: {}.\ndeadline: {}'.format(self.id, self.task, self.deadline) + '\033[0m'


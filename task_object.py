class Task:
    def __init__(self, task) -> None:
        self._id = task[0]
        self._created_date = task[1]
        self._task = task[2]
        self._deadline = task[3]

    @property
    def id(self):
        return self._id
    
    @property
    def created_date(self):
        return self._created_date
    
    @property
    def task(self):
        return self._task
    
    @property
    def deadline(self):
        return self._deadline

from datetime import datetime

class Task:
    def __init__(self, description, status="pending"):
        self.id = None # set by task list when added
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    @classmethod
    def from_dict(cls, data):
        task = cls(data['description'], data['status'])
        task.id = data['id']
        task.created_at = data['created_at']
        task.updated_at = data['updated_at']
        return task

    def to_dict(self):
        return {
            'id': self.id,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, description):
        self.description = description
        self.updated_at = datetime.now().isoformat()

    def mark(self, status):
        self.status = status
        self.updated_at = datetime.now().isoformat()

from django.db import models

class Alert:
    def __init__(self, alert_type, title, lot_number):
        if alert_type not in ("violation", "service request"):
            raise ValueError("alert_type must be either 'violation' or 'service request'")
        
        self.alert_type = alert_type
        self.title = title
        self.lot_number = lot_number

class ToDoItem:
    def __init__(self, id, title, due, completed=False):
        self.id = id
        self.title = title
        self.due = due
        self.completed = completed


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'due': self.due,
            'completed': self.completed,
        }
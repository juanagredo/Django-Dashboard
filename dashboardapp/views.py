from django.shortcuts import render
from .models import Alert, ToDoItem

def index(request):

  alerts = [
        Alert(alert_type="violation", title="Broken Fence", lot_number=101),
        Alert(alert_type="service request", title="Leaking Pipe", lot_number=204),
        Alert(alert_type="violation", title="Noise Complaint", lot_number=312),
        Alert(alert_type="violation", title="Update violation", lot_number=1655)
    ]
  
  todos = [
        ToDoItem(1,"Prepare docs for meeting", "2 DAYS", False),
        ToDoItem(2,"Send mail to Paul", "1 DAY", True),
        ToDoItem(3, "Review Q2 financial report", "3 DAYS", False),
        ToDoItem(4, "Schedule team check-in", "TODAY", False),
        ToDoItem(5, "Fix login bug on dashboard", "1 DAY", True),
        ToDoItem(6, "Prepare slides for stakeholder meeting", "5 DAYS", False),
    ]
  
  todos_data = [todo.to_dict() for todo in todos]
  
  context = {
        "alerts": alerts,
        'todos': todos_data
    }
  return render(request, 'dashboard/index.html', context)
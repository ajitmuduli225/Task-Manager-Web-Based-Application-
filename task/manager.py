from task.models import *

class TaskManager:
    def add_task(self, title, description, priority, status):
        task = Task(title=title, description=description, priority=priority, status=status)
        task.save()
        return task

    def edit_task(self, task_id, title=None, description=None, priority=None, status=None):
        try:
            task = Task.objects.get(id=task_id)
            if title:
                task.title = title
            if description:
                task.description = description
            if priority:
                task.priority = priority
            if status:
                task.status = status
            task.save()
            return task
        except Task.DoesNotExist:
            return None

    def delete_task(self, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return True
        except Task.DoesNotExist:
            return False

    def view_all_tasks(self):
        return Task.objects.all()

    def filter_tasks_by_priority(self, priority):
        return Task.objects.filter(priority=priority)


    def get_task_by_id(self,task_id):
        try:
            task = Task.objects.get(id=task_id)
            return task
        except Task.DoesNotExist:
            return None

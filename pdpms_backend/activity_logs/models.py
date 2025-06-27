from django.db import models

class ActivityLog(models.Model):
    log_id = models.CharField(max_length=255, primary_key=True)
    username = models.CharField(max_length=255)
    action_log = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.log_id} - {self.username}"
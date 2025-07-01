from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position_title = models.TextField(max_length=255)
    employee_status = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'employees'
        managed = False

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"
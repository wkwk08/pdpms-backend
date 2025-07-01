from django.db import models

class Property(models.Model):
    property_no = models.CharField(max_length=255, primary_key=True)
    document_id = models.CharField(max_length=255)
    par_no = models.CharField(max_length=255)
    description = models.TextField()
    serial_no = models.CharField(max_length=255)
    date_acquired = models.DateField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    end_user = models.CharField(max_length=255)
    estimated_life_use = models.IntegerField()
    property_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        db_table = 'properties'
        managed = False

    def __str__(self):
        return f"{self.property_no} - {self.description[:30]}"
    
class ServiceableProperty(models.Model):
    property_no = models.CharField(max_length=255, primary_key=True)
    document_id = models.CharField(max_length=255)
    par_no = models.CharField(max_length=255)
    description = models.TextField()
    serial_no = models.CharField(max_length=255)
    date_acquired = models.DateField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    end_user = models.CharField(max_length=255)
    estimated_life_use = models.IntegerField()
    property_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        db_table = 'serviceable_properties'
        managed = False

    def __str__(self):
        return f"{self.property_no} - {self.description[:30]}"
    
class UnserviceableProperty(models.Model):
    property_no = models.CharField(max_length=255, primary_key=True)
    document_id = models.CharField(max_length=255)
    par_no = models.CharField(max_length=255)
    description = models.TextField()
    serial_no = models.CharField(max_length=255)
    date_acquired = models.DateField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    end_user = models.CharField(max_length=255)
    estimated_life_use = models.IntegerField()
    property_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        db_table = 'unserviceable_properties'
        managed = False

    def __str__(self):
        return f"{self.property_no} - {self.description[:30]}"
    
class ForRepairProperty(models.Model):
    property_no = models.CharField(max_length=255, primary_key=True)
    document_id = models.CharField(max_length=255)
    par_no = models.CharField(max_length=255)
    description = models.TextField()
    serial_no = models.CharField(max_length=255)
    date_acquired = models.DateField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    end_user = models.CharField(max_length=255)
    estimated_life_use = models.IntegerField()
    property_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        db_table = 'for_repair_properties'
        managed = False

    def __str__(self):
        return f"{self.property_no} - {self.description[:30]}"

class CondemnedProperty(models.Model):
    property_no = models.CharField(max_length=255, primary_key=True)
    document_id = models.CharField(max_length=255)
    par_no = models.CharField(max_length=255)
    description = models.TextField()
    serial_no = models.CharField(max_length=255)
    date_acquired = models.DateField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    end_user = models.CharField(max_length=255)
    estimated_life_use = models.IntegerField()
    property_status = models.CharField(max_length=255)
    remarks = models.TextField()

    class Meta:
        db_table = 'condemned_properties'
        managed = False

    def __str__(self):
        return f"{self.property_no} - {self.description[:30]}"
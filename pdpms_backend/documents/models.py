from django.db import models

class Document(models.Model):
    document_id = models.CharField(max_length=255, primary_key=True)
    reference_code = models.CharField(max_length=255)
    subject = models.TextField()
    document_type = models.CharField(max_length=255)
    document_date = models.DateField()
    date_received = models.DateField()
    received_by = models.CharField(max_length=255)
    document_status = models.CharField(max_length=255)
    remarks = models.TextField()
    pdf_file = models.FileField(upload_to='documents/pdfs/', null=True, blank=True)
    base_document_id = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'documents'
        managed = False

    def __str__(self):
        return f"{self.document_id} - {self.subject}"

class CompletedDocument(models.Model):
    document_id = models.CharField(max_length=255, primary_key=True)
    reference_code = models.CharField(max_length=255)
    subject = models.TextField()
    document_type = models.CharField(max_length=255)
    document_date = models.DateField()
    date_received = models.DateField()
    received_by = models.CharField(max_length=255)
    document_status = models.CharField(max_length=255)
    remarks = models.TextField()
    pdf_file = models.FileField(null=True, blank=True)

    class Meta:
        db_table = 'completed_documents'
        managed = False

    def __str__(self):
        return f"{self.document_id} - {self.subject}"
    
class OnGoingDocument(models.Model):
    document_id = models.CharField(max_length=255, primary_key=True)
    reference_code = models.CharField(max_length=255)
    subject = models.TextField()
    document_type = models.CharField(max_length=255)
    document_date = models.DateField()
    date_received = models.DateField()
    received_by = models.CharField(max_length=255)
    document_status = models.CharField(max_length=255)
    remarks = models.TextField()
    pdf_file = models.FileField(null=True, blank=True)

    class Meta:
        db_table = 'ongoing_documents'
        managed = False

    def __str__(self):
        return f"{self.document_id} - {self.subject}"

class ArchivedDocument(models.Model):
    document_id = models.CharField(max_length=255, primary_key=True)
    reference_code = models.CharField(max_length=255)
    subject = models.TextField()
    document_type = models.CharField(max_length=255)
    document_date = models.DateField()
    date_received = models.DateField()
    received_by = models.CharField(max_length=255)
    document_status = models.CharField(max_length=255)
    remarks = models.TextField()
    pdf_file = models.FileField(null=True, blank=True) 

    class Meta:
        db_table = 'archived_documents'
        managed = False

    def __str__(self):
        return f"{self.document_id} - {self.subject}"
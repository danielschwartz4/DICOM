from django.db import models

class Modality(models.TextChoices):
				MRI = 'MRI'
				CT = 'CT'
				US = 'US'
				NA = 'NA'

# Create your models here.
class Instance(models.Model):
    instance_id = models.AutoField(primary_key=True)
    instance_url = models.CharField(max_length = 100, default='https://healthcare.googleapis.com/v1')
    patient_name = models.CharField(max_length = 100)
    date = models.DateField(auto_created=True)
    modality = models.CharField(
        max_length=3,
        choices=Modality.choices,
				default=Modality.NA
    )


    def __str___(self):
        return self.title
from django.db import models


class CSVFile(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d/')

    def __str__(self):
        return self.file.__str__()
# Create your models here.

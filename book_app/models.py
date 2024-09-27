from django.db import models

# Create your models here.
from django.db import models
# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
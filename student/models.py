from django.db import models
from shared.models import BaseModel
# Create your models here.
import uuid
import random

class Student(BaseModel, models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(BaseModel,models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    book_id = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.book_id = str(uuid.uuid4().__str__()).split("-")[-1]
            while Book.objects.filter(book_id=str(self.book_id)).exists():
                self.book_id = str(uuid.uuid4().__str__()) + str(random.randint(1,9))
            super(Book, self).save(*args, **kwargs)


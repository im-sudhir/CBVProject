from django.db import models

# Create your models here.
class CourseModel(models.Model):
    name =models.CharField(max_length=40)
    author=models.CharField(max_length=40)
    price=models.IntegerField()
    discount=models.FloatField(default=0)
    duration=models.DurationField()

    def __str__(self):
        return self.name
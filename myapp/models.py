from django.db import models

# Create your models here.

class ModelOne(models.Model):
    name = models.CharField(max_length=100)
    large_pickle_file = models.FileField()
    sample_input_file = models.FileField()

    def __str__(self):
        return self.name

class ModelTwo(models.Model):
    name = models.CharField(max_length=100)
    model_one = models.ForeignKey(ModelOne, on_delete=models.CASCADE)
    upload_file = models.FileField()

    def __str__(self):
        return self.name
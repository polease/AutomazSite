from django.db import models
import uuid

# Create your models here.

class Mazolution(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    problem_title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    block = models.CharField(max_length=255)
    context = models.CharField(max_length=2000)
    solution_overview = models.CharField(max_length=200)
    shortcut_key_binding = models.CharField(max_length=50)
    environment = models.CharField(max_length=500)

    def __str__(self):
        return self.problem_title

class MazolutionStep(models.Model):
    mazolution = models.ForeignKey(Mazolution,default=None,on_delete=models.CASCADE,related_name="steps")
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    automation = models.CharField(max_length=2000)
    reference_mazolution = models.ForeignKey(Mazolution,default=None,null=True,on_delete=None,related_name="reference_steps")

    def __str__(self):
        return self.name




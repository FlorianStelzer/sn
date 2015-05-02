from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=160)
    deadline = models.DateTimeField()
    finished = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.title
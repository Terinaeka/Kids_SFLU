from django.db import models

class Todo(models.Model):
    title =models.CharField('Назва', max_length=100)

    def __str__(self):
        return self.title
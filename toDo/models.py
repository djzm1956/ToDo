from django.db import models


class SearchTerms(models.Model):
    search = models.CharField(max_length=200)


# Create your models here.
class ToDos(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.task


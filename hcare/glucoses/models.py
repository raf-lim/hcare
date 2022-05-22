from django.db import models
from django.urls import reverse


class Glucose(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='glucoses')
    glucose = models.PositiveSmallIntegerField()
    recorded = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'glucose record {self.id}'

    def get_absolute_url(self):
        return reverse('glucoses:detail', kwargs={'pk': self.id})


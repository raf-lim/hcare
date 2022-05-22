from django.db import models
from django.urls import reverse


class BloodPressure(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='pressures')
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()
    recorded = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'record {self.id}'

    # def get_absolute_url(self):
    #     return reverse('bloodpressures:detail', kwargs={'pk': self.id})

from django.db import models
from django.contrib.auth.models import User


class Insight(models.Model):
    RECOMMENDATION_TYPES = [
        ('saving', 'Saving'),
        ('investment', 'Investment'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='insights')
    recommendation_type = models.CharField(max_length=20, choices=RECOMMENDATION_TYPES)
    description = models.TextField()
    suggested_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.recommendation_type}"
from django.db import models
from django.utils import timezone

# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    upvotes = models.DecimalField(max_digits=10, decimal_places=1)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name
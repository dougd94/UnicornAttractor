from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Feature(models.Model):
    STATUS_CHOICES = (
            ('T', 'To Do'),
            ('D', 'Doing'),
            ('F', 'Finished')
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    upvotes = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , default='')
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='T')
    price = models.DecimalField(max_digits=2, decimal_places=0, default='50')
    paid = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return self.name
        
class Commentf(models.Model):
    """
    Comments for under bug pages
    """
    feature = models.ForeignKey(Feature)
    author = models.ForeignKey(User)
    content = models.TextField(max_length=300, blank=False)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.feature.name, str(self.author.username))
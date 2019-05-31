from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Bug(models.Model):
    StatusOptions = (
            ('T', 'To Do'),
            ('D', 'Doing'),
            ('F', 'Finished')
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    upvotes = models.DecimalField(max_digits=10, decimal_places=0, default='1')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , default='')
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=StatusOptions, default='T')

    def __str__(self):
        return self.name
        
class Comments(models.Model):
    """
    Comments for under bug pages
    """
    bugpk=models.ForeignKey(Bug)
    author = models.ForeignKey(User)
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    
    def __str__(self):
        return str(self.author)
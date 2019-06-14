from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Bug(models.Model):
    STATUS_CHOICES = (
            ('T', 'To Do'),
            ('D', 'Doing'),
            ('F', 'Finished')
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    upvotes = models.DecimalField(max_digits=10, decimal_places=0, default='0')
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='T')

    def __str__(self):
        return self.name

class Votes(models.Model):
    ''' upvote'''
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    bugpk = models.ForeignKey(Bug, on_delete=models.CASCADE)
    class Meta:
        # checks voter and bug against each other to see if upvote allowed
        unique_together = ("voter", "bugpk")
     
    def __str__(self):
        return str(self.voter)
       
class Comment(models.Model):
    """
    Comments for under bug pages
    """
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)
    created_date = models.DateTimeField(null=True, auto_now_add=True)
    
    def __str__(self):
        return '{}-{}'.format(self.bug.name, str(self.author.username))
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
#from groups.models import Group

class Bill(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #group = models.ForeignKey(Group,on_delete=models.CASCADE)
    cost = models.DecimalField(...,max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bill-detail', kwargs={'pk': self.pk})
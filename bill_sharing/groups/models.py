from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('group', 'user'),
    )

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="member_invites",
    )
    invite_reason = models.CharField(max_length=64)



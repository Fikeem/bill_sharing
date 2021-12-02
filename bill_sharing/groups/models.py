from django.db import models
from django.db. models import Count, Sum
from django.contrib.auth.models import User as User
from django.db.models.manager import Manager
from django.utils import timezone
from django.urls import reverse
import hashlib

class GroupManager(models.Manager):
    def get_queryset(self):
        return super(GroupManager, self).get_queryset().select_related('bills', 'users').annotate(user_count=Count('users'))

class Group(models.Model):
    name = models.CharField(max_length=128)
    # members = models.ManyToManyField(
    #     User,
    #     through='User',
    #     through_fields=('group', 'user'),
    # )
    members = models.ManyToManyField(User, through='Membership')
    users_edits = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    objects = GroupManager()

    def __str__(self):
        return self.name
        
    @property
    def invite_code(self):
        timestamp = models.DateTimeField(default=timezone.now)
        digest = hashlib.sha1( str(timestamp) + str(self.pk) ).hexdigest()
        return str(digest)[2:12]

    @property
    def invite_url(self):
        return reverse('invite_detail', kwargs={'pk': self.pk, 'hash': self.invite_code})

    def users_with_totals(self, current_user=None):
        user_list = []
        users = self.users.prefetch_related('bills').all()
        user_total = None

        for user in users:
            bills = user.bills.all().filter(group=self.pk).aggregate(total=Sum('cost'))
            user_dict = {
                'user': user,
                'total': bills['total'] or float('0')
            }
            if current_user and current_user.pk == user.pk:
                user_total = bills['total']

            user_list.append(user_dict)

        if user_total:
            for user_dict in user_list:
                user_dict['relative_total'] = user_dict['total'] - user_total

        return user_list
    
    def get_absolute_url(self):
        return reverse('bill_list', kwargs={'group':self.pk})

                


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # inviter = models.ForeignKey(
    #     User, 
    #     on_delete=models.CASCADE,
    #     related_name="member_invites",
    # )
    # invite_reason = models.CharField(max_length=64)



from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from groups.models import Group
from django.utils.translation import gettext_lazy as _

class Bill(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    cost = models.DecimalField(...,max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bill-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-date_posted','pk']
        get_latest_by = 'date_posted'

class Contribution(models.Model):
    
    bill_from = models.OneToOneField(
        Bill, 
        verbose_name=_('From'), 
        related_name='contrib_from',
        on_delete=models.CASCADE
    )
    bill_assign_to = models.OneToOneField(
        Bill, 
        verbose_name=_('Assign_to'), 
        related_name='contrib_assign_to',
        on_delete=models.CASCADE
    )
    memo = models.TextField(blank=True)

    def __str__(self):
        return _("Contribution to %s") % self.bill_assign_to.user.get_username()

    def delete(self, *args, **kwargs):
        self.bill_from.delete()
        self.bill_assign_to.delete()
        return super(Contribution, self).delete(*args, **kwargs)

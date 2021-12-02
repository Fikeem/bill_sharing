from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Bill
from groups.models import Group
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import ngettext_lazy as _

# Create your views here.

### Video Tutorial
## https://www.youtube.com/watch?v=qDwdMDQ8oX4
###

class InviteCreate(LoginRequiredMixin, DetailView):
    """
    Shows the URL to invite people to join a group
    """
    template_name = "expenses/invite_create.html"
    model = Group

    def get_queryset(self):
        return self.request.user.expense_groups.all()


class InviteDetail(LoginRequiredMixin, DetailView):
    """
    Shows an invitation, provided that you have a valid invite code
    """
    template_name = "expenses/invite_detail.html"
    model = Group

    def get_object(self,queryset=None):
        group = super(InviteDetail, self).get_object()
        if self.kwargs['hash'] == group.invite_code:
            return group
        else:
            raise Http404


class InviteAccept(LoginRequiredMixin, RedirectView):
    """
    Accepts an invitation confirmation via POST, verifies the hash first
    """
    template_name = "expenses/invite_accept.html"
    http_method_names = ['post',]

    def post(self, request, *args, **kwargs):
        group = Group.objects.get(pk=self.kwargs['pk'])
        if self.kwargs['hash'] == group.invite_code:
            group.users.add(request.user)
            messages.add_message(request, messages.SUCCESS, _('Invite accepted! You may now share expenses with the group.'))
            return redirect(group.get_absolute_url())
        else:
            raise Http404
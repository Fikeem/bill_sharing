from django.shortcuts import render, get_object_or_404
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
from django.contrib.auth.models import User
from groups.models import Group
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

# Create your views here.

### Video Tutorial
## https://www.youtube.com/watch?v=qDwdMDQ8oX4
###
def home(request):
    context = {
        'bills': Bill.objects.all()
    }
    return render(request, 'bills/home.html', context)
    #return HttpResponse('<h1> Billing Home </h1>')

class BillViewMixin(object):
    model = Bill

    def get_queryset(self):
        try:
            return self.request.user.bill_groups.get(pk=self.kwargs['group']).bill_set.all()
        except Group.DoesNotExist:
            raise Http404

    def get_form_kwargs(self, **kwargs):
        kwargs = super(BillViewMixin, self).get_form_kwargs(**kwargs)
        kwargs['users'] = self.request.user.bill_groups.get(pk=self.kwargs['group']).users.all()
        return kwargs

    def get_success_url(self):
        return reverse_lazy('bill_list',kwargs={'group':self.kwargs['group']})

class BillListView(LoginRequiredMixin, ListView, BillViewMixin):
    model = Bill
    template_name = 'bills/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'bills'
    ordering = ['-date_posted']
    paginate_by = 20
    search_fields = ['title', 'description']
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Bill.objects.filter(group=user.groups).order_by('-date_posted')

    

class BillDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    
class BillCreateView(LoginRequiredMixin, CreateView):
    model = Bill
    fields = ['title', 'content', 'cost']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bill
    fields = ['title', 'content', 'cost']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        bill = self.get_object()
        if self.request.user == bill.user:
            return True
        return False

class BillDeleteView(LoginRequiredMixin, DeleteView):
    model = Bill
    success_url = '/'

def about(request):
    return render(request, 'about.html',{'title' : 'About'})
    #return HttpResponse('<h1> Billing About</h1>')



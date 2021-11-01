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

# Create your views here.

### Video Tutorial
## https://www.youtube.com/watch?v=qDwdMDQ8oX4
###
def home(request):
    context = {
        'bills': Bill.objects.all()
    }
    return render(request, 'bill_share/home.html', context)
    #return HttpResponse('<h1> Billing Home </h1>')

class BillListView(LoginRequiredMixin, ListView):
    model = Bill
    template_name = 'bill_share/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'bills'
    ordering = ['-date_posted']

class BillDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    
class BillCreateView(LoginRequiredMixin, CreateView):
    model = Bill
    fields = ['title', 'content', 'cost']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Bill
    fields = ['title', 'content', 'cost']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        bill = self.get_object()
        if self.request.user == bill.author:
            return True
        return False

class BillDeleteView(LoginRequiredMixin, DeleteView):
    model = Bill
    success_url = '/'

def about(request):
    return render(request, 'bill_share/about.html',{'title' : 'About'})
    #return HttpResponse('<h1> Billing About</h1>')


    
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
    {
        'author': 'EricF',
        'description': 'Grocery Bill',
        'cost': '$ 212.35',
        'date_posted': 'October 20, 2021'
    },
        {
        'author': 'AnotherUserA',
        'description': 'Name of some other item',
        'cost': 'a currency value',
        'date_posted': 'October 21, 2021'
    }
]
### Video Tutorial
## https://www.youtube.com/watch?v=qDwdMDQ8oX4
###
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'bill_share/home.html', context)
    #return HttpResponse('<h1> Billing Home </h1>')

def about(request):
    return render(request, 'bill_share/about.html',{'title' : 'About'})
    #return HttpResponse('<h1> Billing About</h1>')


    
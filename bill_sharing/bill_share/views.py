from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

bills = [
    {
        'author': 'EricF',
        'description': 'Name of some item',
        'cost': 'some currency value',
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
        'bills': bills
    }
    return render(request, 'bill_share/home.html', context)
    #return HttpResponse('<h1> Billing Home </h1>')

def about(request):
    return render(request, 'bill_share/about.html',{'title' : 'About'})
    #return HttpResponse('<h1> Billing About</h1>')

def login(request):
    return render(request, 'bill_share/login.html',{'title' : 'Login'})

    
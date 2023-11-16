from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    people = [
        {'name': 'abhijeet', 'age':26},
        {'name': 'rohan', 'age':36},
        {'name': 'vicky', 'age':28}
    ]
    vegetables = ['pumpkin', 'tomato', 'potato', 'bhindi']
    return render(request, "hello.html", context= {'people': people, 'vegetables': vegetables})

    
def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")
def success_page(request):
    return HttpResponse("this is a sucess page ig")
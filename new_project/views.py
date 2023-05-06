from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'new_project/home.html')

def contacts_page(request):
    return render(request, 'new_project/contacts.html')
from django.shortcuts import render
from django.views.generic import ListView
from .models import Phone

class IndexView(ListView):
    queryset = Phone.objects.all().order_by('name')
    template_name = 'Phone/list.html'
    context_object_name = 'Phones'

# def list(request):
#     Phones = Phone.objects.all().order_by('name')
#     return render(request, "Phone/list.html", {'Phones' : Phones})

def result(request):
    word = request.GET['word']
    words = Phone.objects.filter(name__contains = word)
    return render(request, "Phone/result.html", {'word' : word, 'contacts' : words})
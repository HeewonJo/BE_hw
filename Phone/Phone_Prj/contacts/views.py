from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
# from django.views.generic import ListView

# class IndexView(ListView):
#     queryset = Phone.objects.all().order_by('name')
#     template_name = 'contacts/list.html'
#     context_object_name = 'Phones'

def list(request):
    Phones = Phone.objects.all().order_by('name')
    return render(request, "contacts/list.html", {'Phones' : Phones})

def result(request):
    word = request.GET['word']
    words = Phone.objects.filter(name__contains = word)
    return render(request, "contacts/result.html", {'word' : word, 'contacts' : words})

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        phone = Phone.objects.create(
            name = name,
            phone_num = phone_num,
            email = email,
        )
        return redirect('list')
    return render(request, 'contacts/create.html')

def detail(request, id):
    phone = get_object_or_404(Phone, id = id)
    return render(request, 'contacts/detail.html', {'phone' : phone})

def update(request, id):
    phone = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        phone.name = request.POST.get('name')
        phone.phone_num = request.POST.get('phone_num')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('detail', id)
    return render(request, 'contacts/update.html', {'phone' : phone})

def delete(request, id):
    phone = get_object_or_404(Phone, id = id)
    if request.method == "POST":
        phone.delete()
        return redirect('list')
    return render(request, 'contacts/delete.html', {'phone' : phone})
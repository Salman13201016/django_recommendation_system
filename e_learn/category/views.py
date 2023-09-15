from django.shortcuts import render, HttpResponse,redirect
from .models import categories


# Create your views here.

def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    name = request.POST.get('cat_name')
    cat_obj = categories()
    cat_obj.name  = name
    cat_obj.save()

    return redirect("cat_index")

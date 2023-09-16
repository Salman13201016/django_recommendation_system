from django.shortcuts import render
from category.models import categories

# Create your views here.

def index(request):
    all_data = categories.objects.all()
    data = {"data":all_data}
    return render(request,'admin/course.html',data)

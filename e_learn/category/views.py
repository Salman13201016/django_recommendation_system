from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request,'admin/cat.html')
def insert(request):
    return HttpResponse(request.POST.get('cat_name'))

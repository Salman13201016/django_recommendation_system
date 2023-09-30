from django.shortcuts import render, HttpResponse,redirect
from category.models import categories
from .models import courses

# Create your views here.

def index(request):

    all_data = categories.objects.all()
    all_course = courses.objects.all()
    data = {"data":all_data,"course_data":all_course}
    return render(request,'admin/course.html',data)

def insert(request):
    cat_id = request.POST.get('cat_id')
    name = request.POST.get('course_name')
    description = request.POST.get('desciption')
    fee = request.POST.get('course_fee')
    discount = request.POST.get('discount')
    image = request.FILES.get('img')
    module = request.POST.get('module')
    print("sss",image)
    category = categories.objects.get(pk=cat_id)
    course_obj = courses()
    course_obj.name = name
    course_obj.cat_id = category
    course_obj.description = description
    course_obj.fee = fee
    course_obj.discount = discount
    course_obj.image = image
    course_obj.module = module
    course_obj.save()

    return redirect('course_index')
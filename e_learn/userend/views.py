from django.shortcuts import render

from category.models import categories
from course.models import courses
from itertools import zip_longest
# Create your views here.

def home(request):
    cat_obj  = categories.objects.all()
    all_data = {'cats':cat_obj}
    
    return render(request,'user/home.html',all_data)


def prod_list(request,id):
    course_obj  = courses.objects.filter(cat_id=id)
    discount_fee_list = []
    for i in course_obj:
        discount_fee = i.fee - ((i.discount * i.fee)/100)
        discount_fee_list.append(discount_fee)

    course_data = zip_longest(course_obj, discount_fee_list)
    all_data = {'course':course_data}
    return render(request,'user/product.html',all_data)

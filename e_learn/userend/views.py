from django.shortcuts import render

from category.models import categories
from course.models import courses
from itertools import zip_longest
# Create your views here.

def home(request):
    cat_obj  = categories.objects.all()
    new_course1  = courses.objects.order_by('-pk')
    feature_data = ''
    course_data=''
    feature_product1  = courses.objects.filter('cat_id_id=2')
    discount_fee_list = []
    discount_fee_list2 = []

    if(len(feature_product1)>1):
        feature_product  = courses.objects.filter('cat_id_id=2').order_by('-pk')[:len(feature_product1)]
        # new_course  = courses.objects.filter('cat_id_id=2').order_by('-pk')[:len(new_course1)]
        for i in feature_product:
            discount_fee = i.fee - ((i.discount * i.fee)/100)
            # discount_fee2 = j.fee - ((j.discount * j.fee)/100)
            discount_fee_list.append(discount_fee)
            # discount_fee_list2.append(discount_fee2)
        # course_data = zip_longest(new_course, discount_fee_list)
        feature_data = zip_longest(feature_product, discount_fee_list)
    if(len(new_course1)>1):
        
        new_course  = courses.objects.order_by('-pk')[:len(new_course1)]
        for i in new_course:
            discount_fee = i.fee - ((i.discount * i.fee)/100)
            
            discount_fee_list2.append(discount_fee)

        course_data = zip_longest(new_course, discount_fee_list2)
        

    elif(len(feature_product1)==1 and len(new_course1)==0):
        feature_data = feature_product1
        course_data = False
    elif(len(feature_product1)==0 and len(new_course1)==1):
        feature_data = False
        course_data = new_course1
    elif(len(feature_product1)==1 and len(new_course1)==1):
        feature_data = feature_product1
        course_data = new_course1
    else:
        feature_data = False
        course_data = False

    
    
    all_data = {'cats':cat_obj,'new_course':course_data,'feature_data':feature_data}
    
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

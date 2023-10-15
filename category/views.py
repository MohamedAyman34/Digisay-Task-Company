from django.shortcuts import render , redirect
from .models import Category
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.




def category_list(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id = category_id)
        category.sub_category_1 = f'SUB {category.parent_category} 1'
        category.sub_category_2 = f'SUB {category.parent_category} 2'
        
        Category.objects.create(parent_category=category.sub_category_1)
        Category.objects.create(parent_category=category.sub_category_2)

        # categories = Category.objects.all()
        # html = render_to_string('category/page.html',{'categories':categories,request:request})
        # return JsonResponse({'result':html})        

    return render(request,'category/page.html',{'categories':categories})
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Post,Category,Brand
from django.db.models import Q
from django.urls import reverse
from .forms import createForm, PostModelForm
import os
# Create your views here.

def main(request):
    return render(request,'main.html')

def brand(request):
    cate_obj = Category.objects.all()
    return render(request,'brandsurch.html',{"cate_key":cate_obj})

def incategory(request,category_id):
    this_category = get_object_or_404(Category, id=category_id)
    take_obj = Post.objects.filter(category = this_category)
    return render(request,'incategoiry.html',{"take_key":take_obj, "this_category":this_category})

def detail(request, detail_id):
    detail = get_object_or_404(Post, pk=detail_id)
    return render(request, 'detail.html', {"detail_key":detail})

def update(request,update_id):
    update_obj = get_object_or_404(Post,pk=update_id)
    form = createForm()
    if request.method == "POST":
        update_obj.name = request.POST['name']
        update_obj.about = request.POST['about']
        update_obj.pic = request.FILES['pic']
        update_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj,"form":form})

def create(request):
    form = PostModelForm()
    category = Category.objects.all()
    brand = Brand.objects.all()
    if request.method == "POST":
        post_val = Post()
        brand_id = request.POST.get('brand',None)
        post_val.brand = brand.get(id=brand_id)
        post_val.title = request.POST['title']
        post_val.text = request.POST['text']
        post_val.pic = request.FILES['pic']
        category_id = request.POST.get('category',None)
        post_val.category = category.get(id=category_id)
        post_val.save()
        return redirect(reverse('brand'))
    else:
        pass

    return render(request, 'create.html',{'form':form, "categoryobj":category, "brandobj":brand})

def delete(request, delete_id):
    delete_obj = get_object_or_404(Post, pk= delete_id)
    delete_obj.delete()
    return redirect('main')  

def searchResult(request):
    query = None
    item = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        item = Post.objects.all().filter(Q(category__name__contains = query) | Q(brand__name__contains = query) | Q(title__contains = query) | Q(text__contains = query))
        if query== "":
            item = None
    return render(request, 'search.html',{'items':item, 'query':query})

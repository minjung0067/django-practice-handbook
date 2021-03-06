from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Post,Category,Brand
from django.db.models import Q
from django.urls import reverse
from .forms import createForm, PostModelForm
from django.contrib.auth.models import User
from django.contrib import auth
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
    form = createForm()
    update_obj = get_object_or_404(Post,pk=update_id)
    category = Category.objects.all()
    brand = Brand.objects.all()
    if request.method == "POST":
        update_obj.brand = brand.get(id=brand_id)
        update_obj.title = request.POST['title']
        update_obj.text = request.POST['text']
        update_obj.pic = request.FILES['pic']
        update_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj, "form":form, "categoryobj":category, "brandobj":brand})

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

# 회원 가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

# 로그 아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    return render(request, 'login.html')


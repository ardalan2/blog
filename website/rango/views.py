from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category , Page
from rango.forms import CategoryForm , PageForm

#----------------------------------------------------------------------

def index(request):
    category_list = Category.objects.order_by('-likes')
    context_dict = {'categories' : category_list}
    page_list = Page.objects.order_by('-views')
    context_dict['pages']=page_list
    return render (request,'index.html',context_dict)
def about(request):
    context_dict={'name':"ardalan",
    }
    return render (request,'about.html',context_dict)

def category (request, category_name_slug):
    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name']=category.name
        pages = Page.objects.filter(category = category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Category.DoesNotExist:
        print "no category"
        
    return render(request, 'category.html', context_dict)
    
def add_category (request):
    print "1"
    if request.method == 'POST':
        print "2"
        form = CategoryForm(request.POST)
        print "3"
        if form.is_valid():
            form.save(commit = True)
            print "4"
            return index(request)
        
        else:
            print form.errors
            
    else:
        form = CategoryForm()
    print "5"    
    return render(request,'add_category.html',{'form':form})

def add_page(request,category_name_slug):
    print "6"
    try:
        cat=Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None
    print "7"
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                print "8"
                page = form.save(commit= False)
                page.category = cat
                page.views =0 
                page.save()
                print "9"
                return category(request,category_name_slug)
        else: print form.errors
    else: form = PageForm()
    print "10"
    context_dict={'form':form,'category':cat}
    print "11"
    return render(request,'add_page.html',context_dict)
    print "12"            

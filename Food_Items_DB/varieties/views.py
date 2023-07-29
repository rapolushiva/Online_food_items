from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from varieties.models import food,Category
from varieties.forms import foodForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required



@login_required()
def showitem(request):
    category = request.GET.get('category')

    if category ==None:
        products=food.objects.filter(Item_Published=True).order_by('Manufactured_Date')

    else:
        products=food.objects.filter(Item_Category__name=category)


    page_num=request.GET.get('page')            #creating the total pages
    paginator = Paginator(products,3)           #seting total number of products in a page:3
    try:
        products=paginator.page(page_num)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages )

    categories =Category.objects.all()
    context={
        'foods':products,
        'categories':categories,
    }
    return render (request,'showitems.html',context)


#itemdetails


def itemdetail(request,pk):
    foods=food.objects.get(id=pk)
    context={
        'x':foods
    }
    return render (request,'itemdetails.html',context)

#add item 
def addProduct(request):
    form=foodForm()

    if request.method=="POST":
        form =foodForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showallitems')
    context={
        "formss":form
    }
    return render(request,'additem.html',context)

#update item

def updateitem(request,pk):
    foods=food.objects.get(id=pk)
    form=foodForm(instance=foods)
    if request.method=='POST':
        form=foodForm(request.POST,request.FILES, instance=foods)
        form.save()
        return redirect('showallitems')
    context={
        'formss':form
    }

    return render(request,'updateitem.html', context)
    

#delete item

def deleteitem(request,pk):
    foods=food.objects.get(id=pk)
    foods.delete()
    return redirect('showallitems')


def searchbar(request):
    if request.method =='GET':
        query=request.GET.get('query')
        if query:
            product=food.objects.filter(Item_Name__contains=query)                                 #999
            return render(request,'searchbar.html',{'foods':product})
        else:
            print("no products in database")
            return render( request,'searchbar.html',{})
# Create your views here.

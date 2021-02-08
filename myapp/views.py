from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Flower
from .forms import MyForm
# Create your views here.


def index(request):

    q = request.GET.get('q',None)

    items = ''

    if q is None or q is "":
        flowers = Flower.objects.all()

    elif q is not None:

        flowers = Flower.objects.filter(title__contains=q)    






    return render(request,'myapp/index.html',{'data':flowers}) 



# udating view 
def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


    else:

        form = MyForm()   

    return render(request,'myapp/create.html',{'form':form})         




# edit view 

def edit(request,pk=None):
    flower = get_object_or_404(Flower,pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST,instance=flower)
        if form.is_valid():
            form.save()
            return redirect('/')


    else:

        form = MyForm(instance=flower)   

    return render(request,'myapp/edit.html',{'form':form})         




# delete view 
def delete(request,pk=None):
    flower = get_object_or_404(Flower,pk=pk)
    flower.delete()
    return redirect('/')










# detail view 
def detail(request,slug=None):
    flower = get_object_or_404(Flower,slug=slug)

    return render(request,'myapp/detail.html',{'datas':flower})






# tags view 

def tags(request,slug=None):

    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request,'myapp/index.html',{'data':flowers})
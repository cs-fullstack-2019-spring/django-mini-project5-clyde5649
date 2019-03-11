from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from.forms import RecipeModel,RecipeForm,Userform
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    allEntries = RecipeForm(request.POST or None)
    context = {
            "allEntries": allEntries
    }
   # return HttpResponse('call me')

    return render(request, 'RecipesApp/index.html',context)


def newrecipepage(request):
    return render(request, 'RecipesApp/newrecipepage.html')



def Addrecipe(request):
    form = RecipeForm(request.POST or None)
    context = {
        'new_form': form
    }
    if request.method =='POST':
        return render(request,'RecipesApp/newrecipepage.hyml',context)







def login(request):

    context = {
        'login': login
    }
    return render(request, 'registration/login.html', context)





def newuser(request):
    form = Userform(request.POST or None)
    context = {
        'new_form': form
    }
    if request.method =="POSt":
        print(request.POST)
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        return render(request,'RecipesApp/newuser.html',context)

    return render(request,'RecipesApp/index')
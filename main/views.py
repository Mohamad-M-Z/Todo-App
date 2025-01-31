from django.shortcuts import render, HttpResponse, redirect
from .models import Plane
from .forms import AddForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

# import for

# Create your views here.


@login_required(login_url="login/")
def list_planen(request):
    planes = Plane.objects.all()
    context = {'planes': planes}
    return render(request,"Todo/todo.html", context)


def AddFormView(request):
    if request.method == "POST":
        form = AddForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = AddForm()
    return render(request, 'Todo/todo.html', {'form':form})


def delete_plane(request,plane_id=None):
    delete=Plane.objects.get(id=plane_id)
    delete.delete()
    return redirect("/")

# def login()
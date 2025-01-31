from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm
from .models import UserLogin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')

                return redirect('login_view')

        form = AuthenticationForm()
        return render(request, 'login/login.html', {"form": form})
    else:
        return redirect('/')


@login_required(login_url='login/')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('../login/')
                # return HttpResponseRedirect(reverse('login-view'))
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'login/signup.html', context)
    else:
        return redirect('/')


#
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse
# from django.http import HttpResponse
# # Create your views here.
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             form = AuthenticationForm(request=request,data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('/')
#
#                 # next_url = request.GET.get('next', 'login_view')
#                 return redirect('login_view')
#
#         form = AuthenticationForm()
#         context = {'form':form}
#         return render(request,'accounts/login.html',context)
#     else:
#         return redirect('/')
#
#
# @login_required(login_url='/accounts/login/')
# def logout_view(request):
#     logout(request)
#     return redirect('/')
#
#
#
# def signup_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('login')
#         form = UserCreationForm()
#         context = {"form":form}
#         return render(request,'accounts/signup.html',context)
#     else:
#         return redirect('/')
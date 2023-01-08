from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class home(View):

    def get(self,request):
        return render(request,'home.html')

    def post(self,request):
        return render(request,'home.html')


class register(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request,'register.html',{'form':form})

    def post(self,request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
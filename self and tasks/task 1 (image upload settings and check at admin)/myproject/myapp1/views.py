from django.shortcuts import render,redirect
from django.views import View
from .forms import myappForm


# Create your views here.

class home(View):

    def get(self,request):
        form = myappForm()
        return render(request,'myapp1/home.html',{'form':form})


    def post(self,request):
        form = myappForm(request.POST,request.FILES)
        print('posted')
        if form.is_valid():
            print('validated')
            form.save()
            print('saved')
            return redirect('thanks')

class thanks(View):

    def get(self,request):
        return render(request,'myapp1/thanks.html')


    def post(self,request):
        pass
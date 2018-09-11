from django.shortcuts import render
from forms import EmpForm
from django.shortcuts import render

# Create your views here.


def create(request):
    form = EmpForm(request.POST)

    if form.is_valid() and request.method=='POST':
        form.save()
    return render(request,'Dummy.html',{'form':form})

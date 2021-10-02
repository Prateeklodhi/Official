from django.shortcuts import redirect, render
from .forms import ClientForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "POST":
        clientform = ClientForm(request.POST)
        if clientform.is_valid():
            clientform.save()
            messages.success(request,"Thank You For Your Response We Will Contact You Soon")
            return redirect('html/index.html')
        else:
            messages.error(request,"Something Is Wrong Sorry For Inconvinience")
    else:
        clientform =ClientForm()    
    return render(request,'html/index.html',{'clientform':clientform})

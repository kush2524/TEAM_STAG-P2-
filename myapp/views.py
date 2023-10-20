from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import sign
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    

    return render(request, 'index.html')

def review(request):
    
    return render(request,'review.html')
    
def signup(request):
    if request.method == 'POST':

        username=request.POST.get('name')
        venue=request.POST.get('venue')
        time=request.POST.get('msg_subject')
        user=sign(username=username,venue=venue,time=time)
        user.save()
        return redirect('blog')
    else:
        return render(request,'signup.html')
def blog(request):
    val=sign.objects.all()
    print(val)

    return render(request,'blog.html',{'val':val})
def contacts(request):
    return render(request,'contacts.html')

    
    
     

        
        

    



    

    
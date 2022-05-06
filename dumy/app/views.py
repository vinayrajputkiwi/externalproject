from django.shortcuts import render,redirect
from .models import signup

# Create your views here.
def sign(request):
    if(request.method=="POST"):
        un=request.POST.get('txtUserName','')
        pwd=request.POST.get('txtPassword','')
        em=request.POST.get('txtEmail','')
        dob=request.POST.get('txtDOB','')
        rec=signup(username=un,password=pwd,email=em,dob=dob)
        rec.save()
        return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    response=render(request,'signin.html')
    if request.method == "POST":
        un=request.POST['txtUserName']
        pwd=request.POST['txtPassword']
        try:
            d1=signup.objects.get(username=un,password=pwd)
        except signup.DoesNotExist:
            return render(request,'signin.html')
        else:  
            request.session['uid'] = d1.id
            return redirect("pro")
    else:
        return render(request,'signin.html')

def profile(request):
    if(request.session.get('uid')):
        uid=request.session['uid']
        d1=signup.objects.get(id=uid)
        return render(request,'profile.html',{'uid':d1})
    else:
        return render(request,'signin.html')

def users(request):
    if(request.session.get('uid')):
        allusers=signup.objects.all()
        return render(request, 'users.html',{'allusers':allusers})
    else:
       return redirect('signin')
# def logout(request):
#     try:
#         del request.session['uid']    
#     except KeyError:        
#     	pass
#     return redirect('signin')
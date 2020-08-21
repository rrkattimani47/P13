from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="rashmi"
    return render(request,"myapp/profile.html",{'name':name})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})


def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="FeMale"
        else:
            gender="Male"
        send_mail("Thanks For Registration","hello Mr./Ms.{} {}\n Thanks for Registering".format(first_name,last_name),
        "akshay.python@gmail.com",[email,],fail_silently=True)
        return redirect("home")
    return render(request,"myapp/registrations.html")


def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,'multiselect.html')

from django.core.files.storage import FileSystemStorage

#uploading and displaying the uploaded image
def img_upld(request):
    return render(request,"img_upld.html")

from myapp.utilities import store_image
def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES.get('sam1')
        image2=request.FILES.get('sam2')
        file_urls=map(store_image,[image1,image2])        
                
    return render(request,"img_display.html",context={'file_urls':file_urls})

from myapp import forms

def builtinforms(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)#im creating a form instance with the data filled the all the firlds will get th
        #the specified value
        if form.is_valid():
            #cleaned_data is varible in form instance that holds the dictonary containing the data that we 
            #have filled
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            image=form.cleaned_data.get('image')
           # store_image(image)
            data=form.cleaned_data
            return render(request,"display_data.html",context=data)
    form=forms.SampleForm()
    return render(request,'builtin.html',{'form':form})

#forms is a file or a library 
#in forms Form is a class so we inherit from forms.Form

from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm , LoginForm
from django.contrib import messages
from .models import CategoryModel,ImageModel
from .forms import ImageForm
# Create your views here.

def SignOut_View(request):
    messages.warning(request,'SuccessFully Logged Out to the System')
    logout(request)
    
    return redirect('home')


class Home_View(View):
    def get(self,request):
        forms = LoginForm()
        context = {'forms':forms}
        return render(request,'home.html',context)
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,' SucceesFully Logged In ')
            return redirect('gallery')
        
        return render(request, 'home.html')


class Register_View(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('gallery')
        
        forms = RegisterForm()
        context = {'forms':forms}
        return render(request,'register.html' ,context)
    
    def post(self,request):
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request,'SuccessFully Registered to the DataBase ')
            return redirect('home')
        context = {"forms":forms}
        return render(request, 'register.html', context)
    

class GalleryView(View):
    def get(self,request):
        category = CategoryModel.objects.all()
        Images = ImageModel.objects.all()
        context = {'category':category, 'Images':Images}
        return render(request,'gallery.html',context)
    
    def post(self,request):
        return render(request, 'gallery.html')
    

class Cat_View(View):
    def get(self,request, id):
        Images = ImageModel.objects.filter(cat = id) # filtered this using match their primary key using in a particular data 
        category = CategoryModel.objects.all() # mention this if not then not show after filtered the particular coloum data
        context = {'Images':Images, 'category':category}
        return render(request,'gallery.html',context)
        


class addimage_view(View):
    def get(self, request):
        forms = ImageForm()
        context = {'forms':forms}

        return render(request, 'addimage.html',context)


    def post(self, request):
        forms = ImageForm(request.POST, request.FILES)
        if forms.is_valid():
            task = forms.save(commit = False) # use false becase no need to save only store data in task variable after come all data then commi 
            task.uploaded_by = request.user  # store uploaded data  into the user model 
            task.save()  # after store then save data 
            messages.success(request,'SuccessFully Your Data Added to the DataBase')
            return redirect('gallery')  # redirect the home page 

        return redirect('addimage')


class MyUpload_View(View):
    def get(self,request):
        Images = ImageModel.objects.filter(uploaded_by = request.user)

        context = {'Images':Images}
        return render(request,'myuploads.html',context)


class View_Info(View):
    def get(self,request,id):
        data = ImageModel.objects.get(id = id) # filtered this using match their primary key using in a particular data 
        category = CategoryModel.objects.all() # mention this if not then not show after filtered the particular coloum data
        context = {'data':data, 'category':category}
        print(data.title)
        return render(request,'viewinfo.html',context)

       
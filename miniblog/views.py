
from django.http import Http404
from django.shortcuts import redirect, render, HttpResponseRedirect
from .forms import SingupForm,LoginForm, AddPostForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import BlogPost
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

# Create your views here.

class PostListView(ListView):
    model = BlogPost
    template_name = 'miniblog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        try:
            return super(PostListView,self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1 
            return super(PostListView,self).get_context_data(*args, **kwargs)   

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'miniblog/readpost.html'

def Index(request):
    post = BlogPost.objects.all().order_by('id')
    paginator = Paginator(post, 3 , orphans=1)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'miniblog/index.html',{'page_obj':page_obj})

    

def About(request):
    return render(request, 'miniblog/about.html')

def Contact(request):
    return render(request, 'miniblog/contact.html')

def Singup(request):
    if request.method == 'POST':
        fm = SingupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'You Have Created Successfully')    
            user = fm.save()
            group = Group.objects.get(name = 'auther')
            user.groups.add(group)

            return HttpResponseRedirect('/signup/')
    else:        
        fm = SingupForm()

    return render(request, 'miniblog/singup.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
    
                user = authenticate(username=uname, password=pwd)
    
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:        
            fm = LoginForm()
        return render(request, 'miniblog/login.html',{'form':fm})   
    else:
        return HttpResponseRedirect('/dashboard/')     


def Dashboard(request):
    if request.user.is_authenticated:
        post = BlogPost.objects.all()
        return render(request, 'miniblog/dashboard.html',{'post':post})
    else:
        return HttpResponseRedirect('/login/')  

def AddPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = AddPostForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/addpost/')
        else:
            fm = AddPostForm()        
        return render(request, 'miniblog/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/') 

def EditPost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(pk=id)
            fm = AddPostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = BlogPost.objects.get(pk=id)
            fm = AddPostForm(instance=pi)        
        return render(request, 'miniblog/editpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')  

def Delete(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = BlogPost.objects.get(pk=id) 
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')                         

def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#change password with old password    

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/dashboard/')
        else:        
           fm = PasswordChangeForm(user=request.user)
           
        return render(request, 'miniblog/changepass.html',{'form':fm})
    else:
        return redirect('/login/')    


# chnage password or forgate password  

def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data= request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/dashboard/')
        else:        
           fm = SetPasswordForm(user=request.user)
           
        return render(request, 'miniblog/changepass.html',{'form':fm}) 
    else:
        return redirect('/login/')         



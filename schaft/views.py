from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UserRegisterForm ,UserUpdateForm, ProfileUpdateForm

# Create your views here.


def home(request): 
    posts = Post.objects.all()
    return render(request, 'home.html', locals())
@login_required
def moringa(request):
    posts = Post.objects.all()
    return render(request, 'moringa.html', locals())  

 
 
def registration_form(request):
   if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Your account has been created! You are now able to log in')
           return redirect('login')
   else:
       form = UserRegisterForm()
   return render(request, 'registration/registration_form.html', {'form': form})


def login(request):
    return render(request, 'registration_form/login.html')   

@login_required
def buruburu(request):
    posts = Post.objects.all()
    return render(request, 'buruburu.html', locals()) 

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        # 'p_form': p_form
    }

    return render(request, 'profile.html', context)
@login_required
def pumwani(request):
    posts = Post.objects.all()
    return render(request, 'pumwani.html', locals()) 

# @login_required
def post(request, id):
   post = Post.objects.get(id=post.id)
   comments = Comment.objects.filter(post=post)
   if request.method == 'POST':
       form = PostForm(request.POST)
       if form.is_valid():
           img = form.save(commit=False)
           img.user = request.user
           img.post = post
           img.save()
           return redirect("home")
   else:
       form = PostForm()
   return render(request, 'post.html', {"post": post, "img": img, "form": form})   
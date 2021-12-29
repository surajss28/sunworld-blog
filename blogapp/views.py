from django.db.models import query
from django.urls.base import reverse
from django.utils.timezone import now
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Mention, Post,Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from blogapp.templatetags import extras
from django.db.models import Q



def post_list(request):
    object_list = Post.objects.all()
    trending = Post.objects.all().filter(trending__contains='Trending')
    paginator = Paginator(object_list, 6) # 6 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/index.html',{'page': page,'posts': posts, 'trending':trending})
    

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   publish__year = year,
                                   publish__month = month,
                                   publish__day = day)
    comments= Mention.objects.all().filter(post=post,parent=None)
    replies= Mention.objects.all().filter(post=post).exclude(parent=None)
    trending = Post.objects.all().filter(trending__icontains='Trending')
    replyDict={}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)
    return render(request,'blog/post/detail.html',{'post': post ,'comments': comments,'user': request.user, 'replyDict': replyDict, 'trending':trending})


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your SunWorld account has been successfully created")
        return redirect('/')

    return render(request,"blog/register.html")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return render(request,'blog/login.html')



def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')



def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'blog/post/contact.html')

class TechnologyListView(ListView):
    queryset = Post.objects.all().filter(blog_category__icontains='Tech')
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post/technology.html'  


class SportsListView(ListView):
    queryset = Post.objects.all().filter(blog_category__icontains='Sports')
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post/sports.html'  


class FoodListView(ListView):
    queryset = Post.objects.all().filter(blog_category__icontains='Food')
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/post/food.html'  


class TravelListView(ListView):
    queryset = Post.objects.all().filter(blog_category__icontains='Travel')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/tourist.html'  

def search(request):
    query=request.GET['query']
    if len(query)<4:
        posts = Post.objects.none()
    else:
        posts = Post.objects.all().filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(blog_category__icontains=query))
    return render(request,'blog/search.html',{'posts': posts})


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(id=postSno)
        comments= Mention.objects.all().filter(post=post,parent=None)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=Mention(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= Mention.objects.get(id=parentSno)
            comment=Mention(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")

        post = Post.objects.get(id=postSno)  
        return redirect(post)


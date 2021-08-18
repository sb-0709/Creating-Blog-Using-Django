from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse('This is home')

def about(request):
    return render(request, 'home/about.html')
    #return HttpResponse('This is about')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'home/contact.html')
    #return HttpResponse('This is contact')
    def search (request):
        query = request.GET['query']
        if len(query)>78:
            allPosts = Post.objects.none()
        else:
            allPostsTitle = Post.objects.filter(title__icontains = query)
            allPostsContent = Post.objects.filter(content__icontains = query)
            allPosts = allPostsTitle.union(allPostsContent)
        if allPosts.count() == 0:
            messages.warning(request, "No search results found. Please refine your query")
        params = {'allPosts' : allPosts, 'query': query}
        return render(request, 'home/search.html',params)
       
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check for errorneous inputs
        # 
        # Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse(' 404 - Not Found')
       

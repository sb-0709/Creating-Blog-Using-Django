from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.
def blogHome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, 'blog/blogHome.html',context)
    #return HttpResponse('This is blogHome')

def blogPost(request,slug):
    return render(request, 'blog/blogPost.html')
    #return HttpResponse(f'This is blogPost:{slug}')
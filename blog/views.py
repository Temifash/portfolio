from django.shortcuts import redirect, render
from .models import NewBlog
from . import forms

# Create your views here.
# def blogHome (request):
#     return render(request, "blog/blogHome.html")

# def addBlog (request):
#     return render(request, "blog/addBlog.html")

# def blogDetails (request):
#     return render(request, "blog/blogDetails.html")

def blogHome(request):
    blogs = NewBlog.objects.all()
    return render(request, "blog/blogHome.html", {'blogs' : blogs})

def blogNew(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blogHome")
    else:
        form = forms.CreatePost()
    return render(request, 'blog/addBlog.html', {'form' : form})

def blogDetails(request, pk):
    blog = NewBlog.objects.get(pk=pk)
    return render(request, "blog/blogDetails.html", {"blog": blog})

def deleteBlog(request, id):
    blog = NewBlog.objects.get(pk=id)
    if reqeust.method == "POST":
        blog.delete()
    return render(request, "blog/delete_confirm.html", {"blog": blog})
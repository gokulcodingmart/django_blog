from django.shortcuts import render
from .models import Post, Comment, Like
from django.contrib.auth.models import User

#from .forms import PostForm

# Create your views here.
def index(request):
	#form = PostForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	form = PostForm()
	if request.method == "POST":
		if request.POST.get('title'):
			title  = request.POST.get('title')
			description  = request.POST.get('description')
			category  = request.POST.get('category')
			Post.objects.create(title=title, description=description, category=category)
		elif request.POST.get('postid'):
			postid  = request.POST.get('postid')
			currentuser = request.user
			postobject = Post.objects.get(id=postid)
			Like.objects.create(count="1", post=postobject, user=currentuser)

	post = Post.objects.order_by('-id')
	return render(request, 'home/index.html', {'post':post})

def about(request):
	post = Post.objects.filter(category="finance").order_by('-id')
	return render(request, 'home/finance.html', {'post':post})

	
def contact(request):
	# form = PostForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	form = PostForm()
    if request.method == "POST":
    	title  = request.POST.get('title')
    	description  = request.POST.get('Description')
    	Post.objects.create(title=title, description=description)
    	
    post = Post.objects.filter(category="travel").order_by('-id')
    return render(request, 'home/travel.html', {'post':post})

def education(request):
	if request.method == "POST":
		title  = request.POST.get('postid')
		print(title)
	post = Post.objects.filter(category="education").order_by('-id')
	return render(request, 'home/education.html', {'post':post})


def business(request):

	post = Post.objects.filter(category="business").order_by('-id')
	return render(request, 'home/business.html', {'post':post})


def comment(request):
	if request.method == "POST":
		post  = request.POST.get('post')
		description  = request.POST.get('description')
		postobject = Post.objects.get(id=post)		
		Comment.objects.create(post=postobject, description=description)
	
	return render(request, 'home/comment.html')


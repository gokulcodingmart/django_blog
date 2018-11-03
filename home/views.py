from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Like
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
>>>>>>> e8dce541aee21b7aefd0822e6ffb52df91687cb0

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
	if request.method == "POST":
		if request.POST.get('title'):
			title  = request.POST.get('title')
			description  = request.POST.get('description')
			
			Post.objects.create(title=title, description=description, category="finance")
	post = Post.objects.filter(category="finance").order_by('-id')
	return render(request, 'home/finance.html', {'post':post})


def contact(request):
	# form = PostForm(request.POST or None)
	# if form.is_valid():
	# 	form.save()
	# 	form = PostForm()
    # if request.method == "POST":
    # 	title  = request.POST.get('title')
    # 	description  = request.POST.get('Description')
    # 	Post.objects.create(title=title, description=description)
	if request.method == "POST":
		if request.POST.get('title'):
			title  = request.POST.get('title')
			description  = request.POST.get('description')
			
			Post.objects.create(title=title, description=description, category="travel")
	
	post = Post.objects.filter(category="travel").order_by('-id')
	return render(request, 'home/travel.html', {'post':post})

def education(request):
	if request.method == "POST":
		if request.POST.get('title'):
			title  = request.POST.get('title')
			description  = request.POST.get('description')
			
			Post.objects.create(title=title, description=description, category="education")
	post = Post.objects.filter(category="education").order_by('-id')
	return render(request, 'home/education.html', {'post':post})


def business(request):
	if request.method == "POST":
		if request.POST.get('title'):
			title  = request.POST.get('title')
			description  = request.POST.get('description')
			
			Post.objects.create(title=title, description=description, category="business")

	post = Post.objects.filter(category="business").order_by('-id')
	return render(request, 'home/business.html', {'post':post})


def comment(request, id):

	#post = Post.objects.get(id=id)
<<<<<<< HEAD
	post = get_object_or_404(Post, id=id)


	# if request.method == "POST":
	# 	post  = request.POST.get('post')
	# 	description  = request.POST.get('description')
	# 	postobject = Post.objects.get(id=post)		
	# 	Comment.objects.create(post=postobject, description=description)
	
	return render(request, 'home/comment.html', {'p':post})

=======
	
	print("comment")

	if request.method == "POST":
		post  = request.POST.get('post')
		currentuser = request.user
		
		description  = request.POST.get('description')
		postobject = Post.objects.get(id=post)		
		Comment.objects.create(post=postobject, description=description, user=currentuser)
	post = get_object_or_404(Post, id=id)
	comment = Comment.objects.all()
	
	return render(request, 'home/comment.html', {'p':post, 'comment':comment})


@csrf_exempt
def ajaxcomment(request):
	
	post  = request.POST.get('post')
	description  = request.POST.get('description')
	currentuser = request.user
	postobject = Post.objects.get(id=post)		
	Comment.objects.create(post=postobject, description=description, user=currentuser)
	data['message'] = "commented"
	return JsonResponse(data)

@csrf_exempt
def like(request):
	postid  = request.POST.get('postid')
	currentuser = request.user
	postobject = Post.objects.get(id=postid)
	Like.objects.create(count="1", post=postobject, user=currentuser)
	
>>>>>>> e8dce541aee21b7aefd0822e6ffb52df91687cb0

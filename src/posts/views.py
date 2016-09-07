from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from .forms import PostForm
from .models import Post
import json

def post_list(request):
    post_list = Post.objects.all()
    form = PostForm()
    context = {
        "post_list": post_list,
        "form": form,
    }
    return render(request, 'posts/post_list.html', context)

def create_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Post(text=post_text, author=request.user)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['postpk'] = post.pk
        response_data['text'] = post.text
        response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        response_data['author'] = post.author.username

        return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        "post":post,
    }
    return render(request, 'posts/post_detail.html', context)

def tablet_layout(request):
    return render(request, 'posts/tablet_layout.html')

def fixed_bar(request):
    return render(request, 'posts/fixed_bar.html')

def social_main(request):
    return render(request, 'posts/social_main.html')
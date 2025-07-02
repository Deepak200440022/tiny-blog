from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q
from .forms import PostFrom
from .models import Post

def post_list(request):
    """
    Display a list of published blog posts.

    If a query parameter 'q' is provided via GET, it filters the posts
    by checking if the query is present in the title or text.

    Returns:
        Rendered HTML response with a list of filtered or all published posts.
    """
    query = request.GET.get("q", "")
    posts = Post.objects.filter(published_date__lte=timezone.now())
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(text__icontains=query)
        )

    posts = posts.order_by("published_date")
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    Display the details of a specific blog post.

    Args:
    request (HttpRequest): The incoming HTTP request containing optional  parameters.
        pk (int): Primary key of the post to retrieve.

    Returns:
        Rendered HTML response with the post details.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """
    Handle creation of a new blog post.

    On GET: display an empty form.
    On POST: validate and save the form data as a new post.

    Returns:
        Redirect to post detail on success, or render form on failure.
    """
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostFrom()
    return render(request, 'blog/post_edit.html', {"form": form})

def post_edit(request, pk):
    """
    Handle editing of an existing blog post.

    On GET: display the form with existing data.
    On POST: validate and save the edited data.

    Args:
         request (HttpRequest): The incoming HTTP request containing optional parameters.
        pk (int): Primary key of the post to edit.

    Returns:
        Redirect to post detail on success, or render form on failure.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostFrom(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    """
    Handle deletion of a blog post.

    Args:
         request (HttpRequest): The incoming HTTP request containing optional parameters.
        pk (int): Primary key of the post to delete.

    On POST: delete the post and redirect to the post list.

    Returns:
        Redirect to the list of posts.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
    return redirect("post_list")

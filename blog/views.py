from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 5, 2026',
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'Second post content',
        'date_posted': 'January 6, 2026',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


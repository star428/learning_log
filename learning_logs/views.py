from django.shortcuts import render


def index(request):
    """学习笔记的首页"""
    return render(request, 'learning_logs/index.html')

# Create your views here.

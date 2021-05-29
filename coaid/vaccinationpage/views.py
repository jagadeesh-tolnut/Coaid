from django.shortcuts import render

# Create your views here.
def vacpage(request):
    render(request, 'vacpage/index.html')
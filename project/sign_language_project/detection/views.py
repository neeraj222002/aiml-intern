from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'detection/home.html')

def predict(request):
    if request.method == "POST":
        uploaded_file = request.FILES["sign_image"]  # get uploaded image
        return HttpResponse(f"File uploaded: {uploaded_file.name}")
    else:
        return HttpResponse("No file uploaded.")

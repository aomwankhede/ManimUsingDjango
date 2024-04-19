from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
import subprocess

def index(request):
    return render(request, 'core/index.html')

def animate(request):
    # Run the Manim command to render the animation
    result = subprocess.run(['manim', 'C:/Users/Viraj Wankhede/Desktop/ManimUsingDjango/manim/core/manimCourse.py'], capture_output=True)
    # Check if the command was successful
    if result.returncode == 0:
        # Return a success message or redirect to a page where the user can download the rendered video
        return JsonResponse({'message': 'Animation rendered successfully. You can download the video.'})
    else:
        # Return an error message
        return JsonResponse({'message': 'Failed to render animation.'}, status=500)
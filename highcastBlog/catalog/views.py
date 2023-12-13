from django.shortcuts import render
from django.http import HttpRequest
from .models import Feedback

MENU = {"HIGHCAST":"/", "Main":"/", "About":"/about"}

def feedback_page(request):
    title = "Feedback"
    feedbacks = Feedback.objects.filter(checkbox=True)
    data = {"menu": MENU, "title": title, "feedbacks": feedbacks}
    return render(request, "feedback.html", context=data)

def thanks_page(request):
    full_name = request.POST['full_name']
    email = request.POST['email']
    feedback = request.POST['feedback']
    checkbox = request.POST.get('checkbox', False)
    Feedback.objects.create(full_name=full_name, email=email, feedback=feedback, checkbox=checkbox)
    title = "Thanks"
    data = {"menu": MENU, "title": title, "full_name": full_name}
    return render(request, "thanks.html", context=data)
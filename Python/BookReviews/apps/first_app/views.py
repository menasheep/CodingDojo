from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request): 
	return render(request, "first_app/index.html")

def process(request, route):
	if request.method == "POST":
		# this brings in the value of response_to_views
		if route == "register":
			response_from_models = User.object.validateUser(request.POST)
		else:
			response_from_models = User.object.loginUser(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errorStr"]:
				messages.error(request, error)
			return redirect("login:index")
	print "*"*20
	print response_from_models["userobj"].id
	request.session["user_id"] = response_from_models["userobj"].id
	print request.session["user_id"]
	return redirect("reviews:mainpage")

def logout(request):
	request.session.flush()
	return redirect("login:index")
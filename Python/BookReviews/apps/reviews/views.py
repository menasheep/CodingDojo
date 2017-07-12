# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Book, Review
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "reviews/mainpage.html")

def add_review(request):
    return render(request, "reviews/add_review.html")

def create_review(request):
    if request.method == "POST":
        response_from_book_models = Book.objects.createBook(request.POST)
        response_from_review_models = Review.objects.createReview(request.POST, request.session["user_id"])
        if not response_from_book_models["status"]:
            for error in response_from_models["errorStr"]:
                messages.error(request, error)
        if not response_from_review_models["status"]:
            for error in response_from_models["errorStr"]:
                messages.error(request, error)
        return redirect("reviews:add_review")
    return redirect("reviews:show_review")

def show_review(request):
    return render(request, "reviews/show_review.html")
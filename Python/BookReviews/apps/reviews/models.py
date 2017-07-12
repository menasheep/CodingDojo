# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User

# Create your models here.

class BookManager(models.Manager):
    def createBook(self, postData):
        errorStr = []
        if len(postData['book_title']) < 1:
            errorStr.append("Book title cannot be empty")
        if len(postData['author']) < 1:
            errorStr.append("Author cannot be empty")
        
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            book = self.create(book_title = postData["book_title"], author = postData["author"])
            response_to_views['status'] = True
            response_to_views['book_obj'] = book
        return response_to_views


class ReviewManager(models.Manager):
    def createReview(self, postData, user_id):
        errorStr = []
        if len(postData['review']) < 1:
            errorStr.append("Review can't be empty")
        
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            review = self.create(book = Book.objects.get(book_title=postData["book_title"]), review = postData["review"], rating = postData["rating"], reviewedby = User.object.get(id=user_id))
            response_to_views['status'] = True
            response_to_views['review_obj'] = review
        return response_to_views

class Book(models.Model):
  book_title = models.TextField(max_length=100)
  author = models.TextField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = BookManager()
  def __str__(self):
    return self.book_title

class Review(models.Model):
  book = models.ForeignKey(Book, related_name="review")
  review = models.TextField(max_length=100)
  rating = models.TextField(max_length=100)
  reviewed_by = models.ForeignKey(User, related_name="book_review")
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  def __str__(self):
    return self.book
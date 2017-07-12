# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from . import views

# Create your models here.

from datetime import datetime

d = date(2013, 12, 22)
print(d.year)
print(d.month)
print(d.day)
print(d.strftime("%Y %m %d"))

today = datetime.date.today()
print today
print 'ctime:', today.ctime()
print 'tuple:', today.timetuple()
print 'ordinal:', today.toordinal()
print 'Year:', today.year
print 'Mon :', today.month
print 'Day :', today.day
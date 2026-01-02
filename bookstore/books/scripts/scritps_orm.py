from django.contrib.auth.models import User
from books.models import *
from django.utils import timezone
from pprint import pprint
from django.db import connection
from django.core.management.base import BaseCommand
import random

def run():
    pass
    # r = Review.objects.filter(rating__gte=6)
    # print(r)
    # r.delete()
    
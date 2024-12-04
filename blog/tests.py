from django.test import TestCase
from .models import Author, Category, Post

class BlogModelTests(TestCase):

    def setUp(self):
        self.author = Author.objects
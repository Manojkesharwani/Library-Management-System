from django.db import models

# Create your models here.
# library/models.py

class Book(models.Model):
    book_id = models.PositiveIntegerField(default=None)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    publisher = models.CharField(max_length=100)
    page_count = models.PositiveIntegerField()
    # stock = models.PositiveIntegerField()
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    outstanding_debt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issued_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    rent_fee = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.member

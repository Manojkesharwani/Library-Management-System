from django import forms
from .models import Book, Member, Transaction


class bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {'book_id':forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Book Id'}),
                   'title':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Book Title'}),
                   'authors':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Author Name'}),
                   'isbn': forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Member Name'}),
                   'publisher':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Publisher Name'}),
                   'page_count':forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Page Count'}),
                   
                }
        
class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"
        widgets = {'name': forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Member Name'}),
                   'email': forms.EmailInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Email'}),
                   'outstanding_debt': forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Outstanding debts'}),
                }

class Transactionform(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
        widgets = {
                'book': forms.Select(attrs={'class': 'form-control', 'style': 'max-width:400px'}),
                'member': forms.Select(attrs={'class': 'form-control', 'style': 'max-width:400px'}),
                'issued_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'max-width:400px', 'placeholder': 'YYYY-MM-DD'}),
                'returned_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'max-width:400px', 'placeholder':'YYYY-MM-DD'}),
                'rent_fee': forms.NumberInput(attrs={'class': 'form-control', 'style': 'max-width:400px', 'placeholder': 'Enter Rent Fees'}), 
                }
        
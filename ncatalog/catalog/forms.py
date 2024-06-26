from django import forms
from .models import Books, Comment

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'path', 'description']
        labels = {
            'title': "Título:",
            'path': "Faça upload:",
            'description': "Descrição:",          
            }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'path': forms.ClearableFileInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': "Comentário:",
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    CHOICES= [
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★')
    ]
    
    star = forms.IntegerField(
        label='별점',
        widget=forms.Select(
            choices = CHOICES,
            attrs={
                'style': 'width: 10rem;'
            }
        )
    )


    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 1
            }
        )
    )
    class Meta:
        model = Review
        fields = ['content', 'star']
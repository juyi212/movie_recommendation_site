from django import forms
from .models import Article, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class ArticleForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())
    content = forms.CharField(widget=SummernoteTextFormField())

class ArticleForm(forms.ModelForm):
    PUR = [
        (1, '자유게시판'),
        (2, '추천게시판'),
        (3, '건의게시판'),
    ]
    purpose = forms.IntegerField(
        label='게시판',
        widget=forms.Select(
                choices = PUR,
                attrs={
                    'style': 'width: 10rem;'
                }
            )
    )
    title = forms.CharField(
        label='제목',
    )
    content = SummernoteTextField()

    class Meta:
        model = Article
        fields = ['purpose', 'title', 'content']
        widgets = {
            'content' : SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 1
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['content']
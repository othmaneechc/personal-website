from django.forms import ModelForm, TextInput, Textarea
from .models import Comment 

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'comment': Textarea(attrs={
                'class': "form-control align-top", 
                'style': 'max-width: 300px;',
                'placeholder': 'Comment',
                'rows': 4,
                'cols': 50
            })
        }

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        article = initial.get('article', None)
        super().__init__(*args, **kwargs)
        if article:
            self.fields['article'].initial = article.title

    def save(self, commit=True):
        comment = super().save(commit=False)
        if not comment.article_id:
            comment.article_id = self.initial.get('article_id')
        if commit:
            comment.save()
        return comment

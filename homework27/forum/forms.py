from django.forms import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nickname', 'comment']

        def clean_comment(self):
            text = self.cleaned_data['text']
            bad_words = ['негр', 'гнида', 'мразь', 'тварь']
            for word in bad_words:
                if word in text:
                    raise forms.ValidationError('Плохие слова')
                return text

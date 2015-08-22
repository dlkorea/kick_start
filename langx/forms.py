from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content', )

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['content'] = forms.CharField(
            widget=forms.Textarea(attrs={'cols': 30, 'rows': 2,'placeholder': 'How may I help you?','id':'text'}))

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content', )
        widgets = {
            'content': forms.TextInput(attrs={'size': 40, 'class':'form-control','style':'width:80%'})
        }
        labels = {
            'content': '',
        }

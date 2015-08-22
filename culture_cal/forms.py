from django import forms
from .models import Article, Reply


class WriteArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image', 'start_date',
                  'start_time', 'end_date', 'end_time')
        widgets = {
            'title': forms.TextInput(attrs={'size': 81}),
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'start_date': forms.DateInput(),
            'start_time': forms.TimeInput(),
            'end_date': forms.DateInput(),
            'end_time': forms.TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(WriteArticle, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            init_txt = ','.join([tag.name for tag in kwargs['instance'].tags.all()])
            self.fields['tags'] = forms.CharField(
                label='tag(복수는 쉼표로 구분)',
                initial=init_txt,
                widget=forms.TextInput(attrs={'size': 81}))
        else:
            self.fields['tags'] = forms.CharField(
                label='tag(복수는 쉼표로 구분)',
                widget=forms.TextInput(attrs={'size': 81}))

    def clean_tags(self):
        tag_list = self.cleaned_data.get('tags').split(',')
        return tag_list


class WriteReply(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': 80,
                    'rows': 3,
                    }),
        }
        labels = {
            'content': (''),
        }

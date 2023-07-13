from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']
       labels = {'name': '', 'lang': '', 'code': ''}
       widgets = {
           'name': TextInput(attrs={'placeholder': 'Название сниппета'}),
           'code': Textarea(attrs={'placeholder': 'Код сниппета'}),
       }
       # C помощью exclude можно указать поля, которые нужно исключить
       # Вместе fields и exclude использовать нельзя
       # exclude = ['lang']

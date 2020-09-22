from django import forms

class AddingQuestionForm(forms.Form):
    CHOICES = (
        ('1', 'Ответ 1'),
        ('2', 'Ответ 2'),
        ('3', 'Ответ 3'),
        ('4', 'Ответ 4'),
    )
    question_text = forms.CharField(label='Вопрос:', max_length=255, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    option1 = forms.CharField(label='Ответ №1:', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    option2 = forms.CharField(label='Ответ №2:', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    option3 = forms.CharField(label='Ответ №3:', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    option4 = forms.CharField(label='Ответ №4:', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    correct_answer = forms.ChoiceField(label='Правильный Ответ:', choices=CHOICES, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
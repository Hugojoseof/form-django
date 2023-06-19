from django import forms

class AlunoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    data_nascimento = forms.DateField()

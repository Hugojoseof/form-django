from django.shortcuts import render
from .forms import AlunoForm
from .models import Aluno
# Create your views here.

def cadastro_aluno(request):

    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            data_nascimento = form.cleaned_data['data_nascimento']
            #salvando o aluno no banco.
            # Aluno.objects.create(nome=nome, email=email,data_nascimento=data_nascimento)
            print("Nome: {} - Email:{} - Data de Nascimento:{}".format(nome,email,data_nascimento))
    else:
        print("->>>> entrou primeiro aqui")
        form = AlunoForm()

    return render(request, 'form/index.html', {'form': form})

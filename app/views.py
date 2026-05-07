from django.shortcuts import render, redirect
from .models import Tarefa

# Create your views here.

def index(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        return render(request, 'index.html', {'tarefas': tarefas})      
    return render(request, 'index.html')

def adicionar(request):
    if request.method == 'POST': 
        titulo = request.POST.get('titulo')
        Tarefa.objects.create(titulo=titulo)
    return redirect('index')

def excluir(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('index')

def editar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if request.method == 'POST':
        tarefa.concluida = request.POST.get('concluida') == 'on'
        tarefa.save()
    return redirect('index')
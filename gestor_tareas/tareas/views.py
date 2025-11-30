import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TareaForm

TAREAS_FILE = 'tareas/tareas.json'

def cargar_tareas():
    try:
        with open(TAREAS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(TAREAS_FILE, 'w') as f:
        json.dump(tareas, f, indent=4)

@login_required
def lista_tareas(request):
    usuario = request.user.username
    todas = cargar_tareas()
    mis_tareas = [t for t in todas if t['usuario'] == usuario]
    return render(request, 'tareas/lista_tareas.html', {'tareas': mis_tareas})

@login_required
def detalle_tarea(request, id):
    usuario = request.user.username
    todas = cargar_tareas()
    tarea = next((t for t in todas if t['id'] == id and t['usuario'] == usuario), None)
    if not tarea:
        return redirect('lista_tareas')
    return render(request, 'tareas/detalle_tarea.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            todas = cargar_tareas()
            nueva_tarea = {
                'id': max([t['id'] for t in todas], default=0) + 1,  # ID automático
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'usuario': request.user.username
            }
            todas.append(nueva_tarea)
            guardar_tareas(todas)
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/agregar_tarea.html', {'form': form})

@login_required
def eliminar_tarea(request, id):
    usuario = request.user.username
    todas = cargar_tareas()
    todas = [t for t in todas if not (t['id'] == id and t['usuario'] == usuario)]
    guardar_tareas(todas)
    return redirect('lista_tareas')

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_usuario')
    else:
        form = UserCreationForm()
    return render(request, 'tareas/registro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('lista_tareas')
    else:
        form = AuthenticationForm()
    return render(request, 'tareas/login.html', {'form': form})

@login_required
def logout_usuario(request):
    logout(request)
    return redirect('login_usuario')

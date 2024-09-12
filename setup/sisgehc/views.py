from rest_framework import viewsets, generics
from django.shortcuts import render
from sisgehc.models import Aluno, Curso, Evento
from sisgehc.serializer import AlunoSerializer, CursoSerializer, EventoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all() 
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os eventos"""
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer



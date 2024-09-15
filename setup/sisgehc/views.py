from rest_framework import viewsets, generics
from django.shortcuts import render
from sisgehc.models import Aluno, Curso, Evento, Professor
from sisgehc.serializer import AlunoSerializer, CursoSerializer, EventoSerializer, ProfessorSerializer


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


class ProfessorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os professores"""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


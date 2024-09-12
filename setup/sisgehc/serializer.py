from rest_framework import serializers
from sisgehc.models import Aluno, Curso, Evento

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'horasComplementares', 'curso', 'matricula', 'senha']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nome', 'horasComplementares', 'curso', 
                  'professor', 'dataInicio', 'dataFim', 
                  'horarioInicio', 'horarioFim', 'limiteInscricao', 
                  'descricao', 'imagem']
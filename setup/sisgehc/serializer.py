from rest_framework import serializers
from sisgehc.models import Aluno, Curso, Evento, Professor

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
                  'horaInicio', 'horaFim', 'limiteInscricao', 
                  'descricao', 'imagem']
        

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
from django.db import models
from datetime import date
from .pessoa import Pessoa

# Create your models here.
class Coordenador(Pessoa):
    pass

class Aluno(Pessoa):
    ra = models.IntegerField()
    foto = models.TextField(max_length=255)

class Professor(Pessoa):
    apelido = models.TextField(max_length=255)

class AdministracaoDisciplina(models.Model):
    data = models.DateField(),
    status = models.IntegerField()
    coordenador_id: models.IntegerField()

class AceiteMinistrarDisciplina(models.Model):
    professor_id = models.IntegerField()
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    criterio_avaliacao = models.TextField(max_length=1000)
    plano_aula = models.TextField(max_length=1000)

class Disciplina(models.Model):
    nome = models.TextField(max_length=255, unique=True)
    ementa = models.TextField(max_length=5000)
    plano_ensino = models.TextField(max_length=5000)
    conteudo_programatico = models.TextField(max_length=5000)
    bibliografia_basica = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    competencias = models.TextField(max_length=1000)
    habilidades = models.TextField(max_length=1000)
    carga_horaria = models.IntegerField()
    percentual_teorico = models.DecimalField(max_digits=13, decimal_places=2)
    percentual_pratico = models.DecimalField(max_digits=13, decimal_places=2)

class DisciplinaOfertada(models.Model):
    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=5)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    disciplina_id = models.IntegerField()
    coordenador_id = models.IntegerField()
    aceite_ministrar_disciplina_id = models.IntegerField()
    class Meta:
        unique_together = ('curso', 'turma', 'ano', 'semestre')

class SolicitacaoMatricula(models.Model):
    dt_solicitacao = models.DateField()
    aluno_id = models.IntegerField()
    disciplina_ofertada_id = models.IntegerField()
    coordenador_id = models.IntegerField()

class LiberacaoMatricula(models.Model):
    dt_inicio = models.DateTimeField()
    dt_termino = models.DateTimeField()
    disciplina_ofertada_id = models.IntegerField()
    coordenador_id = models.IntegerField()

class AprovacaoSolicitacaoMatricula(models.Model):
    status = models.IntegerField()
    solicitacao_matricula_id = models.IntegerField()

class Atividade(models.Model):
    titulo = models.TextField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    extras = models.TextField(max_length=255)
    professor_id = models.IntegerField()
    vinculo_atividade_disciplina_ofertada_id = models.IntegerField()

class VinculoAtividadeDisciplinaOfertada(models.Model):
    disciplina_ofertada_id = models.IntegerField()
    professor_id = models.IntegerField()
    status = models.IntegerField()
    dt_inicio = models.DateTimeField()
    dt_encerramento = models.DateTimeField()
    rotulo = models.TextField(max_length=255)

class Avaliacao(models.Model):
    nota = models.IntegerField()
    data = models.DateField()
    obs = models.TextField(max_length=255)
    professor_id = models.IntegerField()

class EntregaAtividade(models.Model):
    aluno_id = models.IntegerField()
    atividade_id = models.IntegerField()
    avaliacao_id = models.IntegerField()
    resposta = models.TextField(max_length=255)
    data = models.DateField()
    status = models.IntegerField()
    titulo = models.TextField(max_length=100)

class Mensagem(models.Model):
    assunto = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    referencia = models.TextField(max_length=255)
    dt_envio = models.DateField()
    dr_resposta = models.DateField()
    resposta = models.TextField(max_length=1000)
    professor_id = models.IntegerField()
    aluno_id = models.IntegerField()
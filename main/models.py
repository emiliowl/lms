from django.db import models
from datetime import date

# Create your models here.
class Usuario(models.Model):
    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login = models.TextField(max_length=20, unique=True)
    senha = models.TextField(max_length=20)

class Coordenador(Usuario):
    pass

class Aluno(Usuario):
    ra = models.IntegerField()
    foto = models.TextField(max_length=255)

class Professor(Usuario):
    apelido = models.TextField(max_length=255)

class Disciplina(models.Model):
    nome = models.TextField(max_length=255, unique=True)
    data = models.DateField()
    status = models.TextField(max_length=255)
    plano_ensino = models.TextField(max_length=5000)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=1000)
    habilidades = models.TextField(max_length=1000)
    ementa = models.TextField(max_length=5000)
    conteudo_programatico = models.TextField(max_length=5000)
    bibliografia_basica = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    percentual_pratico = models.DecimalField(max_digits=13, decimal_places=2)
    percentual_teorico = models.DecimalField(max_digits=13, decimal_places=2)
    coordenador = models.ForeignKey(Coordenador)

class Curso(models.Model):
    nome = models.TextField(max_length=255, unique=True)

class DisciplinaOfertada(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    ano = models.IntegerField()
    semestre = models.IntegerField()
    turma = models.TextField(max_length=1)
    metodologia = models.TextField(max_length=255)
    recursos = models.TextField(max_length=255)
    criterio_avaliacao = models.TextField(max_length=1000)
    plano_aula = models.TextField(max_length=1000)
    disciplina = models.ForeignKey(Disciplina)
    professor = models.ForeignKey(Professor)
    coordenador = models.ForeignKey(Coordenador)
    curso = models.ForeignKey(Curso)

    class Meta:
        unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')

class SolicitacaoMatricula(models.Model):
    dt_solicitacao = models.DateField()
    status = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno)
    disciplina = models.ForeignKey(Disciplina)
    coordenador = models.ForeignKey(Coordenador)

class Atividade(models.Model):
    titulo = models.TextField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    tipo = models.TextField(max_length=255)
    extras = models.TextField(max_length=255)
    professor = models.ForeignKey(Professor)

class AtividadeVinculada(models.Model):
    status = models.IntegerField()
    rotulo = models.TextField(max_length=255)
    atividade = models.ForeignKey(Atividade)
    professor = models.ForeignKey(Professor)
    disciplina_ofertada = models.ForeignKey(DisciplinaOfertada)

class EntregaAtividade(models.Model):
    titulo = models.TextField(max_length=100)
    resposta = models.TextField(max_length=255)
    dt_entrega = models.DateField()
    status = models.IntegerField()
    nota = models.IntegerField()
    dt_avaliacao = models.DateField()
    obs = models.TextField(max_length=255)
    aluno = models.ForeignKey(Aluno)
    atividade_vinculada = models.ForeignKey(AtividadeVinculada)
    professor = models.ForeignKey(Professor)

class Mensagem(models.Model):
    assunto = models.TextField(max_length=255)
    referencia = models.TextField(max_length=255)
    conteudo = models.TextField(max_length=255)
    status = models.IntegerField()
    dt_envio = models.DateField()
    dr_resposta = models.DateField()
    resposta = models.TextField(max_length=1000)
    aluno = models.ForeignKey(Aluno)
    professor = models.ForeignKey(Professor)
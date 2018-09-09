# Generated by Django 2.1.1 on 2018-09-09 19:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AceiteMinistrarDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_id', models.IntegerField()),
                ('metodologia', models.TextField(max_length=255)),
                ('recursos', models.TextField(max_length=255)),
                ('criterio_avaliacao', models.TextField(max_length=1000)),
                ('plano_aula', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AdministracaoDisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AprovacaoSolicitacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('solicitacao_matricula_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=255, unique=True)),
                ('descricao', models.TextField(max_length=255)),
                ('conteudo', models.TextField(max_length=255)),
                ('tipo', models.TextField(max_length=255)),
                ('extras', models.TextField(max_length=255)),
                ('professor_id', models.IntegerField()),
                ('vinculo_atividade_disciplina_ofertada_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('data', models.DateField()),
                ('obs', models.TextField(max_length=255)),
                ('professor_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255, unique=True)),
                ('ementa', models.TextField(max_length=5000)),
                ('plano_ensino', models.TextField(max_length=5000)),
                ('conteudo_programatico', models.TextField(max_length=5000)),
                ('bibliografia_basica', models.TextField(max_length=1000)),
                ('bibliografia_complementar', models.TextField(max_length=1000)),
                ('competencias', models.TextField(max_length=1000)),
                ('habilidades', models.TextField(max_length=1000)),
                ('carga_horaria', models.IntegerField()),
                ('percentual_teorico', models.DecimalField(decimal_places=2, max_digits=13)),
                ('percentual_pratico', models.DecimalField(decimal_places=2, max_digits=13)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.TextField(max_length=255)),
                ('turma', models.TextField(max_length=5)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('disciplina_id', models.IntegerField()),
                ('coordenador_id', models.IntegerField()),
                ('aceite_ministrar_disciplina_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EntregaAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno_id', models.IntegerField()),
                ('atividade_id', models.IntegerField()),
                ('avaliacao_id', models.IntegerField()),
                ('resposta', models.TextField(max_length=255)),
                ('data', models.DateField()),
                ('status', models.IntegerField()),
                ('titulo', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LiberacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inicio', models.DateTimeField()),
                ('dt_termino', models.DateTimeField()),
                ('disciplina_ofertada_id', models.IntegerField()),
                ('coordenador_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.TextField(max_length=255)),
                ('conteudo', models.TextField(max_length=255)),
                ('referencia', models.TextField(max_length=255)),
                ('dt_envio', models.DateField()),
                ('dr_resposta', models.DateField()),
                ('resposta', models.TextField(max_length=1000)),
                ('professor_id', models.IntegerField()),
                ('aluno_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
                ('email', models.TextField(max_length=255)),
                ('celular', models.TextField(max_length=20)),
                ('dt_expiracao', models.DateField(default=datetime.date(1900, 1, 1))),
                ('login', models.TextField(max_length=20, unique=True)),
                ('senha', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoMatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_solicitacao', models.DateField()),
                ('aluno_id', models.IntegerField()),
                ('disciplina_ofertada_id', models.IntegerField()),
                ('coordenador_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VinculoAtividadeDisciplinaOfertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disciplina_ofertada_id', models.IntegerField()),
                ('professor_id', models.IntegerField()),
                ('status', models.IntegerField()),
                ('dt_inicio', models.DateTimeField()),
                ('dt_encerramento', models.DateTimeField()),
                ('rotulo', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pessoa')),
                ('ra', models.IntegerField()),
                ('foto', models.TextField(max_length=255)),
            ],
            bases=('main.pessoa',),
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pessoa')),
            ],
            bases=('main.pessoa',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Pessoa')),
                ('apelido', models.TextField(max_length=255)),
            ],
            bases=('main.pessoa',),
        ),
        migrations.AlterUniqueTogether(
            name='disciplinaofertada',
            unique_together={('curso', 'turma', 'ano', 'semestre')},
        ),
    ]

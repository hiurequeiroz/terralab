# Generated by Django 4.2.9 on 2024-07-26 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aldeia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("populacao", models.IntegerField()),
                ("ano", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="AreaDireto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="AreaGeral",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Atividade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=255)),
                ("descricao", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="AtividadeRegistro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_inicio", models.DateField()),
                ("data_final", models.DateField()),
                ("desafios", models.CharField(max_length=255)),
                ("propostas", models.CharField(max_length=255)),
                ("sucesso", models.CharField(max_length=255)),
                ("melhores_praticas", models.CharField(max_length=255)),
                ("fotos", models.ImageField(upload_to="fotos/")),
                (
                    "atividade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.atividade"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AtividadeRegistroIndicador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta_realizada", models.FloatField()),
                ("data", models.DateField()),
                (
                    "atividade_registro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistro",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CR",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("coordenador", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="DSEI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("coordenador", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Equipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("cargo", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Escola",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("esfera", models.CharField(max_length=255)),
                ("coordenador", models.CharField(max_length=255)),
                (
                    "aldeia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.aldeia"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Financiador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("sigla", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="IGATI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tipo", models.CharField(max_length=255)),
                ("nome", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Indicador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=255)),
                ("descricao", models.CharField(max_length=255)),
                ("reporte", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Instituicao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("sigla", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="OIsLocal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("sigla", models.CharField(max_length=255)),
                ("endereco", models.CharField(max_length=255)),
                ("cnpj", models.CharField(max_length=255)),
                ("nome_repr", models.CharField(max_length=255)),
                ("cargo_repr", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="OIsRegional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ois_reg", models.CharField(max_length=255)),
                ("ois_reg_sigla", models.CharField(max_length=255)),
                ("endereco", models.CharField(max_length=255)),
                ("cnpj", models.CharField(max_length=255)),
                ("nome_repr", models.CharField(max_length=255)),
                ("cargo", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Projeto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("nome_fant", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TIs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("area", models.FloatField()),
                ("fase", models.CharField(max_length=255)),
                ("etnia", models.CharField(max_length=255)),
                ("municipio", models.CharField(max_length=255)),
                ("uf", models.CharField(max_length=255)),
                ("modalidade", models.CharField(max_length=255)),
                ("cr_id", models.IntegerField()),
                ("dsei_id", models.IntegerField()),
                (
                    "oilocal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.oislocal"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Treinados",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("projeto", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TIsIGATI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "igati",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.igati"
                    ),
                ),
                (
                    "tis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.tis"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjetoTI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "projeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.projeto"
                    ),
                ),
                (
                    "tis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.tis"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjetoOI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "oilocal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.oislocal"
                    ),
                ),
                (
                    "projeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.projeto"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Professores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "escola",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.escola"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Produtos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Posto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "aldeia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.aldeia"
                    ),
                ),
                (
                    "dsei",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.dsei"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Polo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "dsei",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.dsei"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Planos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Parcerias",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OIRegLoc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "oilocal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.oislocal"
                    ),
                ),
                (
                    "oiregional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.oisregional",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modelos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Meta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("base", models.FloatField()),
                ("meta", models.FloatField()),
                ("data", models.DateField()),
                (
                    "atividade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.atividade"
                    ),
                ),
                (
                    "indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.indicador"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Leis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Indigena",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("etnia", models.CharField(max_length=255)),
                ("genero", models.CharField(max_length=255)),
                ("cpf", models.CharField(max_length=255)),
                ("rg", models.CharField(max_length=255)),
                ("data_nasc", models.DateField()),
                (
                    "aldeia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.aldeia"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FormacaoIndigena",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("formacao", models.CharField(max_length=255)),
                (
                    "indigena",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.indigena"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EquipeProjeto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "equipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.equipe"
                    ),
                ),
                (
                    "projeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.projeto"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="equipe",
            name="instituicao",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.instituicao"
            ),
        ),
        migrations.CreateModel(
            name="CTL",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("coordenador", models.CharField(max_length=255)),
                (
                    "cr",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.cr"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contratos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Componente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("codigo", models.CharField(max_length=255)),
                (
                    "instituicao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.instituicao",
                    ),
                ),
                (
                    "projeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.projeto"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Casai",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "dsei",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.dsei"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Capacitados",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("projeto", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="atividaderegistroindicador",
            name="indicador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.indicador"
            ),
        ),
        migrations.CreateModel(
            name="AtividadeRegistroEquipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "atividade_registro",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistro",
                    ),
                ),
                (
                    "equipe_projeto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.equipeprojeto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="atividaderegistro",
            name="componente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.componente"
            ),
        ),
        migrations.AddField(
            model_name="atividaderegistro",
            name="equipe_adicional",
            field=models.ManyToManyField(
                related_name="atividades_registradas", to="ieb.equipeprojeto"
            ),
        ),
        migrations.AddField(
            model_name="atividaderegistro",
            name="equipe_projeto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.equipeprojeto"
            ),
        ),
        migrations.AddField(
            model_name="atividaderegistro",
            name="projeto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.projeto"
            ),
        ),
        migrations.AddField(
            model_name="atividade",
            name="componente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.componente"
            ),
        ),
        migrations.CreateModel(
            name="AreaRestrito",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                ("tipo", models.CharField(max_length=255)),
                ("tis", models.CharField(max_length=255)),
                (
                    "atividade_registro_indicador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ieb.atividaderegistroindicador",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AreaGeralTIs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "areageral",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.areageral"
                    ),
                ),
                (
                    "tis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.tis"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="areageral",
            name="atividade_registro_indicador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ieb.atividaderegistroindicador",
            ),
        ),
        migrations.CreateModel(
            name="AreaDiretoTIs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "areadireto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.areadireto"
                    ),
                ),
                (
                    "tis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.tis"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="areadireto",
            name="atividade_registro_indicador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="ieb.atividaderegistroindicador",
            ),
        ),
        migrations.AddField(
            model_name="aldeia",
            name="tis",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ieb.tis"
            ),
        ),
        migrations.CreateModel(
            name="AIS",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
                (
                    "dsei",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ieb.dsei"
                    ),
                ),
            ],
        ),
    ]

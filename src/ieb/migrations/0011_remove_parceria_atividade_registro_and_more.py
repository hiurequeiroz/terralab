# Generated by Django 5.0.6 on 2024-09-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ieb', '0010_remove_parcerias_nome_remove_parcerias_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parceria',
            name='atividade_registro',
        ),
        migrations.AlterField(
            model_name='parcerias',
            name='parcerias',
            field=models.ManyToManyField(related_name='parcerias', to='ieb.parceria'),
        ),
    ]
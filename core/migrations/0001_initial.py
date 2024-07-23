# Generated by Django 5.0.7 on 2024-07-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CadastroCliente",
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
                ("nome", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=11)),
                ("mensagem", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="CadastroFormulario",
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
                ("nome", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("mensagem", models.TextField()),
            ],
        ),
    ]
# Generated by Django 5.2.3 on 2025-07-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('data_edition', models.DateField(auto_now=True)),
                ('data_criacao', models.DateField(auto_now=True)),
            ],
        ),
    ]

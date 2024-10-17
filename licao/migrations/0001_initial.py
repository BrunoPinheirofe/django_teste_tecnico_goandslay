# Generated by Django 5.1.2 on 2024-10-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('conteudo_html', models.TextField()),
            ],
            options={
                'verbose_name': 'Lição',
                'verbose_name_plural': 'Lições',
            },
        ),
    ]

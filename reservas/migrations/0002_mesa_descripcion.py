# Generated by Django 5.0.3 on 2024-03-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesa',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]

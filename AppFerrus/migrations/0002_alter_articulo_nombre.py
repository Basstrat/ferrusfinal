# Generated by Django 3.2.9 on 2022-10-27 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFerrus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(max_length=45, null=True),
        ),
    ]

# Generated by Django 4.2.9 on 2024-01-28 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckbapp', '0007_battle_codekata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='codeKata',
            field=models.FileField(upload_to='code_katas/'),
        ),
    ]

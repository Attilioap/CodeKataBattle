# Generated by Django 4.2.9 on 2024-02-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckbapp', '0017_rename_repositories_repository'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='evaluated',
            field=models.BooleanField(default=False),
        ),
    ]

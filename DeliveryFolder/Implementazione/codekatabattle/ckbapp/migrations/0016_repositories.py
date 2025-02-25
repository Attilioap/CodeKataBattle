# Generated by Django 4.2.9 on 2024-01-31 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ckbapp', '0015_battle_has_started'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ckbapp.battle')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ckbapp.student')),
            ],
        ),
    ]

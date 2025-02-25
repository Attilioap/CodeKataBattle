# Generated by Django 4.2.9 on 2024-01-27 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('maxStudentsForTeam', models.IntegerField()),
                ('registrationDeadline', models.DateField()),
                ('submissionDeadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Educator',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registrationDeadline', models.DateField()),
                ('endingDate', models.DateField()),
                ('description', models.TextField()),
                ('educators', models.ManyToManyField(related_name='tournaments_managed', to='ckbapp.educator')),
                ('students', models.ManyToManyField(related_name='tournaments_participated', to='ckbapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('numTeammates', models.IntegerField()),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ckbapp.battle')),
                ('members', models.ManyToManyField(related_name='teams_joined', to='ckbapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='educators',
            field=models.ManyToManyField(related_name='battles_managed', to='ckbapp.educator'),
        ),
        migrations.AddField(
            model_name='battle',
            name='teams',
            field=models.ManyToManyField(related_name='battles_participated', to='ckbapp.team'),
        ),
        migrations.AddField(
            model_name='battle',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battles', to='ckbapp.tournament'),
        ),
    ]

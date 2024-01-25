# Generated by Django 4.2.9 on 2024-01-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ckbapp', '0003_alter_educator_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educator',
            options={},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='educator',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_confirmed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AddField(
            model_name='user',
            name='fullName',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='educators',
            field=models.ManyToManyField(related_name='tournaments_managed', to='ckbapp.educator'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='students',
            field=models.ManyToManyField(related_name='tournaments_participated', to='ckbapp.student'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.BooleanField(),
        ),
    ]

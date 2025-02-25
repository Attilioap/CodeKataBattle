# Generated by Django 4.2.9 on 2024-01-29 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ckbapp', '0012_alter_team_battle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('battle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='ckbapp.battle')),
                ('invited_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_received', to='ckbapp.student')),
                ('inviting_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations_sent', to='ckbapp.student')),
            ],
        ),
    ]

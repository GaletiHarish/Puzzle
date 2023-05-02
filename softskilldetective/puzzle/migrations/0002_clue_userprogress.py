# Generated by Django 4.2 on 2023-05-02 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('puzzle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('is_dead_end', models.BooleanField(default=False)),
                ('is_solution', models.BooleanField(default=False)),
                ('next_clue', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='puzzle.clue')),
            ],
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('time_taken_per_clue', models.JSONField(default=dict)),
                ('attempts_per_clue', models.JSONField(default=dict)),
                ('current_clue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='puzzle.clue')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

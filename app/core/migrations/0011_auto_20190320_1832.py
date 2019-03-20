# Generated by Django 2.1.7 on 2019-03-20 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190320_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskToEvaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('question', models.TextField()),
                ('points_to_achieve', models.IntegerField()),
                ('is_open_task', models.BooleanField(default=False)),
                ('students_answer', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='examsheetevaluation',
            name='score_in_percents',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='is_open_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taskforstudent',
            name='is_open_task',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskforstudent',
            name='students_answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tasktoevaluate',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_task_eval', to='core.ExamSheetEvaluation'),
        ),
        migrations.AddField(
            model_name='tasktoevaluate',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-18 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0002_auto_20190318_1550")]

    operations = [
        migrations.AlterField(
            model_name="taskforstudent",
            name="students_answer",
            field=models.CharField(blank=True, max_length=255, null=True),
        )
    ]

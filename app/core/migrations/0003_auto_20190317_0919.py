# Generated by Django 2.1.7 on 2019-03-17 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190317_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examsheet',
            name='total_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-30 07:52

import django.db.models.deletion
import django.db.models.query
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.last, on_delete=django.db.models.deletion.CASCADE, to='todo_app.priority'),
        ),
    ]

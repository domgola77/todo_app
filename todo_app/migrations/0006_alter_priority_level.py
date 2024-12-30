# Generated by Django 5.1.4 on 2024-12-29 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_priority_task_priority_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='level',
            field=models.CharField(choices=[('Low', 'Low'), ('High', 'High')], max_length=50, unique=True),
        ),
    ]

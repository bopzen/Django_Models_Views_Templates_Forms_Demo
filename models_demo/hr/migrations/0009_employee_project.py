# Generated by Django 3.2.19 on 2023-06-07 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0008_remove_employee_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='project',
            field=models.ManyToManyField(to='hr.Project'),
        ),
    ]

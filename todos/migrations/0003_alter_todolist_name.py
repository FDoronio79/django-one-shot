# Generated by Django 4.0.6 on 2022-07-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_todolist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]

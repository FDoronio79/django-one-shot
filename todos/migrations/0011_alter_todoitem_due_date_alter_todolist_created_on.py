# Generated by Django 4.0.6 on 2022-07-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0010_alter_todoitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

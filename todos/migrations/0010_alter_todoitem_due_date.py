# Generated by Django 4.0.6 on 2022-07-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0009_alter_todoitem_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-30 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='name',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_hobby_hobby_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devlanguage',
            old_name='dev_language',
            new_name='name',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-14 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tag',
            new_name='name',
        ),
    ]
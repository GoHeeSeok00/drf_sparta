# Generated by Django 4.0.5 on 2022-06-18 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_test_rename_is_activated_event_is_activate_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]

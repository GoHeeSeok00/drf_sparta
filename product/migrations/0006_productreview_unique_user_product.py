# Generated by Django 4.0.5 on 2022-06-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productreview_rating'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='productreview',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='unique_user_product'),
        ),
    ]
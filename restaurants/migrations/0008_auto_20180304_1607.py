# Generated by Django 2.0.2 on 2018-03-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_ifavorite_rfavorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='author',
            new_name='owner',
        ),
    ]

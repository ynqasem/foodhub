# Generated by Django 2.0.2 on 2018-02-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='publish_date',
            field=models.DateField(null=True),
        ),
    ]

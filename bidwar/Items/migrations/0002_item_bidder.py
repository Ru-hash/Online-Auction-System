# Generated by Django 3.0.5 on 2021-04-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bidder',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

# Generated by Django 3.1 on 2020-08-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userIntro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='profilePic',
            field=models.TextField(max_length=250),
        ),
    ]

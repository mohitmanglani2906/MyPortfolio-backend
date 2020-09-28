# Generated by Django 3.1 on 2020-08-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(blank=True, upload_to='images/')),
                ('introduction', models.TextField(max_length=1000)),
            ],
        ),
    ]

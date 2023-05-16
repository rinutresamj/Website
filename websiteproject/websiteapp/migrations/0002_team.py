# Generated by Django 4.2 on 2023-04-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photo')),
                ('shortbio', models.TextField()),
            ],
        ),
    ]

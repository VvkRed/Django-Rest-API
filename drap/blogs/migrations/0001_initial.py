# Generated by Django 4.0.4 on 2022-04-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=30)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=225)),
                ('password', models.CharField(max_length=225)),
            ],
        ),
    ]

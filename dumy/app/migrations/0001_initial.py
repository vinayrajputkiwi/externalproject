# Generated by Django 2.2.12 on 2022-05-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('dob', models.CharField(max_length=40)),
            ],
        ),
    ]
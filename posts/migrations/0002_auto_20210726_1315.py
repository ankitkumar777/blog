# Generated by Django 3.1.4 on 2021-07-26 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='Post',
        ),
    ]
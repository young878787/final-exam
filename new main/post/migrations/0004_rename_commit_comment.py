# Generated by Django 5.1.2 on 2025-01-03 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_useraccount_avatar'),
        ('post', '0003_commit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commit',
            new_name='Comment',
        ),
    ]
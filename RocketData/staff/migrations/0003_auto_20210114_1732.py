# Generated by Django 3.1.4 on 2021-01-14 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='Position',
            new_name='position',
        ),
    ]

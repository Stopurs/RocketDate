# Generated by Django 3.1.4 on 2021-01-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_remove_staffmodels_object_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmodels',
            name='date_employment',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-08 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('C_O_API_App', '0002_indexes_opening_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indexes',
            old_name='symbolISIN',
            new_name='symbolisin',
        ),
    ]

# Generated by Django 3.1.5 on 2021-07-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C_O_API_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexes',
            name='opening_price',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.0 on 2020-03-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20200313_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='date',
            field=models.DateField(null=True),
        ),
    ]

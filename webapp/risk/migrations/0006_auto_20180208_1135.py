# Generated by Django 2.0.2 on 2018-02-08 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0005_auto_20180207_0212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='riskformfieldoption',
            old_name='text',
            new_name='label',
        ),
    ]
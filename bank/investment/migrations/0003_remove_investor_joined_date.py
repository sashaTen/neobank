# Generated by Django 4.2.3 on 2024-08-04 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_rename_inverstor_investor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='joined_date',
        ),
    ]
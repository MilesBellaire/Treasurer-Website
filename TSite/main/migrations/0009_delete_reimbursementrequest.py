# Generated by Django 4.0.4 on 2022-05-30 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_payrequest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReimbursementRequest',
        ),
    ]
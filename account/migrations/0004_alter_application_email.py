# Generated by Django 3.2.2 on 2021-05-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
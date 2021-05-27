# Generated by Django 3.2.2 on 2021-05-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_user_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rate',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='speciality',
            field=models.CharField(blank=True, choices=[('African Cuisine', 'African Cuisine'), ('Mediterian Cuisine', 'Mediterian Cuisine'), ('American Cuisine', 'American Cuisine'), ('none', 'none')], default='none', max_length=30),
        ),
    ]

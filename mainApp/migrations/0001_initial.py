# Generated by Django 3.2.2 on 2021-05-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Lunch', 'Lunch'), ('BreakFast', 'BreakFast'), ('Dinner', 'Dinner')], default='Dinner', max_length=40)),
            ],
        ),
    ]
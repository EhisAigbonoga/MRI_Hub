# Generated by Django 3.0 on 2021-06-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default='Best Selling Author', max_length=100),
        ),
    ]

# Generated by Django 3.0 on 2021-06-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crihhome', '0008_auto_20210624_1914'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OpeningLatest',
        ),
        migrations.RemoveField(
            model_name='latest',
            name='image',
        ),
        migrations.AddField(
            model_name='latest',
            name='image_url',
            field=models.CharField(default='crihhome/images/CRIH.PNG', max_length=2000),
        ),
    ]

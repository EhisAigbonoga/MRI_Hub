# Generated by Django 3.0 on 2021-06-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crihhome', '0002_auto_20210529_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestoncrih',
            old_name='Deadline',
            new_name='deadline',
        ),
        migrations.RemoveField(
            model_name='latestoncrih',
            name='posted_by',
        ),
        migrations.AlterField(
            model_name='latestoncrih',
            name='image_url',
            field=models.ImageField(default='default.jpg', upload_to='opportunity_photos'),
        ),
    ]

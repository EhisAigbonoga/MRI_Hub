# Generated by Django 3.0 on 2021-06-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crihhome', '0014_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='images1.jpg', upload_to='post_image'),
        ),
    ]
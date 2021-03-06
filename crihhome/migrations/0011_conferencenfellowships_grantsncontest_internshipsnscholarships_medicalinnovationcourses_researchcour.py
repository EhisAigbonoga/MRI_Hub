# Generated by Django 3.0 on 2021-06-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crihhome', '0010_auto_20210625_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferencenFellowships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2000)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GrantsnContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2000)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InternshipsnScholarships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=2000)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalInnovationCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=2000)),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ResearchCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.CharField(max_length=2000)),
            ],
        ),
    ]

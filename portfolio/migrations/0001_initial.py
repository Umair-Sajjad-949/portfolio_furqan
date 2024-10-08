# Generated by Django 5.1 on 2024-08-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=255)),
                ('site_logo', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('cover_title', models.CharField(max_length=255)),
                ('cover_desc', models.TextField()),
                ('about_title', models.TextField(max_length=255)),
                ('about_desc', models.TextField()),
                ('facebook', models.TextField(max_length=255)),
                ('linkdeIn', models.TextField(max_length=255)),
                ('Instagram', models.TextField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('github', models.TextField(max_length=255)),
            ],
        ),
    ]

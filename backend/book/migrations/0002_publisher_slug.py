# Generated by Django 2.2.7 on 2019-11-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]

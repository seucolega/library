# Generated by Django 3.1.7 on 2021-03-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20191129_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='gtin',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
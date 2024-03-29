# Generated by Django 2.2.7 on 2019-11-25 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AgeClassification',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Age Classification',
                'verbose_name_plural': 'Age Classifications',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('title', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                (
                    'age_classification',
                    models.ManyToManyField(to='book.AgeClassification'),
                ),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='PersonProfile',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PersonType',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Person Type',
                'verbose_name_plural': 'Person Types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TextualClassification',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Textual Classification',
                'verbose_name_plural': 'Textual Classifications',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'book',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='book.Book',
                    ),
                ),
                (
                    'person',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to='book.PersonProfile',
                    ),
                ),
                ('type', models.ManyToManyField(to='book.PersonType')),
            ],
            options={
                'verbose_name': 'Person (Book)',
                'verbose_name_plural': 'People (Book)',
                'ordering': ['person__name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='book.Publisher',
            ),
        ),
        migrations.AddField(
            model_name='book',
            name='textual_classification',
            field=models.ManyToManyField(to='book.TextualClassification'),
        ),
    ]

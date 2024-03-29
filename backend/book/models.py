from django.db import models
from django.template.defaultfilters import slugify


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class AgeClassification(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Age Classification'
        verbose_name_plural = 'Age Classifications'
        ordering = ['name']

    def __str__(self):
        return self.name


class TextualClassification(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Textual Classification'
        verbose_name_plural = 'Textual Classifications'
        ordering = ['name']

    def __str__(self):
        return self.name


class PersonType(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Person Type'
        verbose_name_plural = 'Person Types'
        ordering = ['name']

    def __str__(self):
        return self.name


class PersonProfile(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    age_classification = models.ManyToManyField(AgeClassification)
    # TODO: Transformar relacionamento com classificação textual em ManyToOne
    textual_classification = models.ManyToManyField(TextualClassification)
    ean = models.CharField(max_length=13, blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title']

    def __str__(self):
        return self.title


class Person(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonProfile, on_delete=models.PROTECT)
    type = models.ManyToManyField(PersonType)

    class Meta:
        verbose_name = 'Person (Book)'
        verbose_name_plural = 'People (Book)'
        ordering = ['person__name']

    @property
    def type_verbose(self):
        return ', '.join([t.name for t in self.type.only('name')])

    @property
    def title(self):
        return f'{self.person.name} ({self.type_verbose})'

    def __str__(self):
        return self.title

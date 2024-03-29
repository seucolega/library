from book.models import (
    AgeClassification,
    Book,
    Person,
    PersonProfile,
    PersonType,
    Publisher,
    TextualClassification,
)
from django.template.defaultfilters import slugify
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import metabooks_api
from .serializers import (
    AgeClassificationSerializer,
    BookInventorySerializer,
    BookSerializer,
    PersonProfileSerializer,
    PersonSerializer,
    PersonTypeSerializer,
    PublisherSerializer,
    TextualClassificationSerializer,
)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer


class AgeClassificationViewSet(viewsets.ModelViewSet):
    queryset = AgeClassification.objects.all().order_by('name')
    serializer_class = AgeClassificationSerializer


class TextualClassificationViewSet(viewsets.ModelViewSet):
    queryset = TextualClassification.objects.all().order_by('name')
    serializer_class = TextualClassificationSerializer


class PersonTypeViewSet(viewsets.ModelViewSet):
    queryset = PersonType.objects.all().order_by('name')
    serializer_class = PersonTypeSerializer


class PersonProfileViewSet(viewsets.ModelViewSet):
    queryset = PersonProfile.objects.all().order_by('name')
    serializer_class = PersonProfileSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('person__name')
    serializer_class = PersonSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer

    @action(detail=False, methods=['post'])
    def inventory(self, request):
        try:
            ean = self.request.data['ean']
            quantity = self.request.data['quantity']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.filter(ean=ean).first()
        if not book:
            # TODO: se nao tiver, verificar no metabooks
            metabooks_instance = metabooks_api.MetabooksAPI()
            metabooks_json = metabooks_api.get_product_json_from_ean(
                metabooks_instance=metabooks_instance, product_ean=ean
            )
            if metabooks_json:
                book = Book(ean=ean)
                for title in metabooks_json.get('titles', []):
                    if title.get('titleType') == '01':
                        book.title = title.get('title')

                # for title in metabooks_json.get("textContents", []):
                #     if title.get("textType") == "03":
                #         book.description = title.get("text")

                if len(metabooks_json.get('publishers', [])):
                    publisher_name = metabooks_json['publishers'][0][
                        'publisherName'
                    ]
                    publisher, created = Publisher.objects.get_or_create(
                        slug=slugify(publisher_name),
                        defaults={'name': publisher_name},
                    )
                    book.publisher = publisher

        if book:
            # TODO: criar função para fazer a entrada de um item no estoque
            book.stock_quantity += int(quantity)
            book.save()

            serializer = BookInventorySerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

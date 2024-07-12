from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price', )

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'title is not alphabetic'
                }
            )

        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    'status': False,
                    'message': 'title and author is not unique'
                }
            )
        return data

    def validate_price(self, price):
        if price < 0:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'price is less than zero'
                }
            )
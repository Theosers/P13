import pytest
from django.test import Client, TestCase
from django.urls import reverse
from .models import Letting, Address


@pytest.mark.django_db
class TestLettings(TestCase):
    client = Client()

    def test_lettings_index(self):
        url = reverse('lettings:lettings_index')
        self.checkAssertion(url, b"Lettings")

    def test_letting_detail(self):
        address = Address.objects.create(
            number=1,
            street='Main',
            city='Lima',
            state='PE',
            zip_code=12345,
            country_iso_code='123'
        )
        letting = Letting.objects.create(
            title='Test Title',
            address_id=address.id
        )
        url = reverse('lettings:lettings', args=(letting.id,))
        self.checkAssertion(url, b'Test Title')

    def checkAssertion(self, url, arg1):
        response = self.client.get(url)
        assert arg1 in response.content
        assert response.status_code == 200

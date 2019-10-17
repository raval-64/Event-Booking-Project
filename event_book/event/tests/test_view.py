from django.test import TestCase, Client
from django.urls import resolve, reverse
from event.views import index, booksummary, eventdetail
from event.models import event,booking

class TestViews(TestCase):
    
    def setUp(self): 
        self.index_url = reverse('event:index')
    
    def test_event_list_index(self):
        self.client = Client()
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
    
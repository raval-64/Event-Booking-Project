from django.test import SimpleTestCase
from django.urls import resolve, reverse
from event.views import index, booksummary, eventdetail


class TestUrls(SimpleTestCase):
    
    def test_event_list_urls_is_resolved(self):
        url = reverse('event:index')
        self.assertEqual(resolve(url).func, index)
    
    def test_event_view_urls_is_resolved(self):
        url = reverse('event:event_view', args=['1'])
        self.assertEqual(resolve(url).func, eventdetail)
    
    def test_booking_summary_is_resolved(self):
        url = reverse('event:book_summary')
        self.assertEqual(resolve(url).func, booksummary)
    
from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('', views.index, name='index'),
    path('event/book-summary/', views.booksummary, name='book_summary'),
    path('event/<int:id>/', views.eventdetail, name='event_view'),
]
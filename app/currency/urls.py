from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailView,

    ContactUsListView,
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsDeleteView,

    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,

)

app_name = 'currency'

urlpatterns = [
    path('rate/list/',  RateListView.as_view(), name='rate-list'),
    path('source/list/',  SourceListView.as_view(), name='source-list'),
    path('message/list/', ContactUsListView.as_view(), name='message-list'),

    path('rate/create/',  RateCreateView.as_view(), name='rate-create'),
    path('contact/create/',  ContactUsCreateView.as_view(), name='contact-create'),
    path('source/create/',  SourceCreateView.as_view(), name='source-create'),

    path('rate/update/<int:pk>/',  RateUpdateView.as_view(), name='rate-update'),
    path('contact/update/<int:pk>/',  ContactUsUpdateView.as_view(), name='contact-update'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),

    path('rate/delete/<int:pk>/',  RateDeleteView.as_view(), name='rate-delete'),
    path('contact/delete/<int:pk>/',  ContactUsDeleteView.as_view(), name='contact-delete'),
    path('source/delete/<int:pk>/',  SourceDeleteView.as_view(), name='source-delete'),

    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),

]

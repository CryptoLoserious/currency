from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_list,
    message_list,
    source_list,
    source_create,
    rate_create,
    contactUs_create,
    rate_update,
    contactUs_update,
    source_update,
    rate_delete,
    contactUs_delete,
    source_delete,
    source_details,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/',  rate_list),
    path('source/list/',  source_list),
    path('message/list/', message_list),
    path('rate/create/',  rate_create),
    path('contact/create/',  contactUs_create),
    path('source/create/',  source_create),
    path('rate/update/<int:pk>/',  rate_update),
    path('contact/update/<int:pk>/',  contactUs_update),
    path('source/update/<int:pk>/',  source_update),
    path('rate/delete/<int:pk>/',  rate_delete),
    path('contact/delete/<int:pk>/',  contactUs_delete),
    path('source/delete/<int:pk>/',  source_delete),
    path('source/details/<int:pk>/',  source_details),

]

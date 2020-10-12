from django.conf.urls import url
from . import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns= [
    url('relative',views.relative,name='relative'),
    url('other',views.other,name='other'),
]

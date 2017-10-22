from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: setup/
    url(r'^signup/', views.signup, name='signup'),
]


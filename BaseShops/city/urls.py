from django.conf.urls import url
from . import views
#views.CityView.as_view()
urlpatterns = [
    url('^$', views.CityView),
]
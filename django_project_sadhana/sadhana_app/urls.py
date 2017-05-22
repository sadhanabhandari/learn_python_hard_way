from django.conf.urls import include, url
from sadhana_app import views


urlpatterns = [
    url(r'^submit',views.my_page),
    url(r'^mypage/$',views.welcome)
]
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()

#definition of routers

router.register('Author',views.AuthorViewSet,basename='Author')
router.register('Quote',views.QuoteViewSet,basename='Quote')
# router.register('quote/random',views.get_random_quote,basename='random')

urlpatterns = [
    path('',include(router.urls)),
    path('quote/random',views.get_random_quote)
]

from django.urls import path
from .views import indexView,galleryView,asView,bookingView,failedView,blogView,loginView,resView,logoutView
from . import views
app_name="hotel"

urlpatterns = [
   path('', indexView.as_view(),name="index"),
   path('gallery/', galleryView.as_view(), name="gallery"),
   path('as/', asView.as_view(), name="as"),
   path('booking/', bookingView.as_view(), name="booking"),
   path('404page/', failedView.as_view(), name="404"),
   path('blog/', blogView.as_view(), name="blog"),
   path('login/',loginView.as_view(),name="login"),
   path('res/',resView.as_view(),name="res"),
   path('logout/',logoutView.as_view(),name="logout"),
]

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
# router.register("services/<int:id>",views.ServiceInfoView,basename="service-info")
urlpatterns = [
    path('services/', views.ServicesView.as_view()),
    path('services/<int:id>/', views.ServiceInfoView.as_view()),
    path('beauticians/', views.BeauticianView.as_view()),
    path('beauticians/male', views.MaleBeauticianView.as_view()),
    path('beauticians/<int:id>/', views.BeauticianDetailView.as_view()),
    path('timeslots/', views.TimeslotView.as_view()),
    path('timeslots/<int:id>/', views.TimeslotDetailView.as_view()),
    path('services/category/<int:id>/', views.ServiceByCategoryView.as_view()),
    path('cart/add',views.CartAddView.as_view()),
    path('addons/category/<int:id>',views.AddonsByCategory.as_view())
]+router.urls

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingView, basename='booking')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
]

urlpatterns += router.urls

from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name = 'index'),  
    path('menu/',views.MenuItemView.as_view(), name  = 'menu'),
    path('menu/<int:pk>,', views.SingleMenuItemView.as_view(), name = 'singlemenu'),
    path('booking/', views.BookingViewSet.as_view({'get': 'list'}), name = 'booking'),
 
]

from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('', views.Sign_in.as_view(),name='signin'),
    path('signup', views.sign_up,name='signup'),
    path('home/<int:id>', views.HomeView,name='home'),
    path('signout', views.Sign_in.sign_out,name='signout'),
    path('product', views.ProductView.as_view(),name='product'),
    path('delete/<int:id>', views.delete_cust ,name='delete'),
    path('deactivate/<int:id>', views.Status_activate.status_deactivate ,name='deactivate'),
    path('activate/<int:id>', views.Status_activate.as_view() ,name='activate'),
#    path('add_to_cart', views.Order.as_view(),name='add_to_cart'),

    path('edit/<int:id>', views.edit,name='edit'),
]



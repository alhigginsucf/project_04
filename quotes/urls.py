from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    #path('<str:tid>', views.home, name='ticker'),
    path('trade.html', views.trade, name="trade"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('history.html', views.history, name="history"),
    path('add_trade', views.add_trade, name="add_trade"),
    path('reset',  views.reset, name="reset"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path
from conta import views



urlpatterns = [
    path('<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    path('', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('login/', views.UsuarioLoginView.as_view(), name='usuario_conta'),
]

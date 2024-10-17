from django.urls import path

from licao.views import LicaoListView, LicaoDetailView, LicaoCreateView, LicaoUpdateHtmlView, LicaoDeleteView


urlpatterns = [
    path('', LicaoListView.as_view(), name='licao-list'),
    path('<int:pk>/', LicaoDetailView.as_view(), name='licao-detail'),
    path('create/', LicaoCreateView.as_view(), name='licao-create'),
    path('<int:pk>/editar-html/', LicaoUpdateHtmlView.as_view(), name='licao-editar-html'),
    path('<int:pk>/delete/', LicaoDeleteView.as_view(), name='licao-delete'),
]


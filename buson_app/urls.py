from django.urls import path

from . import views

app_name = 'buson_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('configuracoes', views.configuracoes, name='configuracoes'),
    path('rotas', views.rotas, name='rotas'),
    path('cadastrar-colaborador', views.cadastrarColaborador, name='cadastrar-colaborador'),
]
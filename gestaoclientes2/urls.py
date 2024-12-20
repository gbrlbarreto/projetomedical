"""gestaoclientes2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from agendamentos import urls as agendamentos_urls
from clientes import urls as clientes_urls
from home import urls as home_urls
from swagger import urls as swagger_urls
from medicos import urls as medicos_urls
from agendamentos.api import urls as agendamentos_urls_rest
from clientes.api import urls as clientes_urls_rest
from medicos.api import urls as medicos_urls_rest
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include(home_urls)),
    path('', include(swagger_urls)),
    path('api-auth/', include('rest_framework.urls')), #exibir "Log in" tela rest
    path('agendamentos/', include(agendamentos_urls)),
    path('clientes/', include(clientes_urls)),
    path('medicos/', include(medicos_urls)),
    path('api/agendamentos', include(agendamentos_urls_rest)),
    path('api/clientes', include(clientes_urls_rest)),
    path('api/medicos', include(medicos_urls_rest)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


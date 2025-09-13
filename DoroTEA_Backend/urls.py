"""
URL configuration for DoroTEA_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/

============================================================
                  SISTEMA DE ROTAS DO DOROTEA
============================================================

Este arquivo é o "mapa de navegação" do seu servidor Django.
Ele define qual URL leva a qual parte da sua aplicação.

Cada entrada na lista urlpatterns associa um endereço web a uma
função ou view que processará a requisição.

ESTRUTURA ATUAL DO SISTEMA DE ROTAS:
1. Página inicial (raiz do domínio) → home_view personalizada
2. Painel administrativo → /admin/
3. API de emoções → /api/ (inclui todas as URLs do app emotions)
4. Servidor de arquivos de mídia → /media/ (apenas em desenvolvimento)

============================================================
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# View personalizada para a página inicial
def home_view(request):
    """
    Página inicial personalizada do projeto Dorotea.
    Esta função retorna um HTML simples com links para as principais áreas.
    
    Quando alguém acessa http://localhost:8000/, vê esta página.
    """
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Servidor Dorotea</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { 
                text-decoration: none; 
                color: #007bff;
                padding: 8px 15px;
                border: 1px solid #007bff;
                border-radius: 4px;
                display: inline-block;
            }
            a:hover { background-color: #f8f9fa; }
        </style>
    </head>
    <body>
        <h1>Servidor Dorotea Funcionando! ✅</h1>
        <p>Endpoints disponíveis:</p>
        <ul>
            <li><a href='/api/emotions/'>API de Emoções</a></li>
            <li><a href='/admin/'>Painel Admin</a></li>
        </ul>
        <p>Acesse <a href='/api/emotions/'>/api/emotions/</a> para ver a API REST</p>
    </body>
    </html>
    """)

# Lista de padrões de URL - a "tabela de roteamento" do projeto
urlpatterns = [
    # Página inicial: http://localhost:8000/
    path('', home_view, name='home'),
    
    # Painel administrativo: http://localhost:8000/admin/
    path('admin/', admin.site.urls),
    
    # API principal: http://localhost:8000/api/
    # Inclui todas as URLs definidas no arquivo emotions/urls.py
    path('api/', include('emotions.urls')),
]

# Adiciona suporte para servir arquivos de mídia durante o desenvolvimento
# Isso permite acessar imagens via URL: http://localhost:8000/media/nome_da_imagem.jpg
# EM PRODUÇÃO: Esta configuração não é usada - um servidor web (Nginx/Apache) deve servir os arquivos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
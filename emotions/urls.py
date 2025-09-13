from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmotionRecordViewSet
from emotions.views import home_view  # Nota: Esta importação não está sendo usada

"""
============================================================
            CONFIGURAÇÃO DE URLs DA APLICAÇÃO EMOTIONS
============================================================

Este arquivo define todas as rotas (URLs) específicas da aplicação Emotions.
Ele é incluído no arquivo principal de URLs do projeto em:
DoroTEA_Backend/urls.py através do path('api/', include('emotions.urls'))

Todas as URLs definidas aqui terão o prefixo '/api/' na URL final.

Funcionamento:
1. O DefaultRouter do Django REST Framework cria automaticamente
   URLs padrão para operações CRUD (Create, Read, Update, Delete)
2. As URLs são registradas no router e depois incluídas em urlpatterns

Estrutura de URLs geradas:
- GET    /api/emotions/     - Lista todos os registros
- POST   /api/emotions/     - Cria um novo registro
- GET    /api/emotions/{id}/ - Detalhes de um registro específico
- PUT    /api/emotions/{id}/ - Atualiza um registro específico
- DELETE /api/emotions/{id}/ - Exclui um registro específico

============================================================
"""

# Cria um roteador padrão do Django REST Framework
router = DefaultRouter()

# Registra a ViewSet EmotionRecordViewSet no router
# Isso automaticamente cria todas as URLs CRUD para o modelo EmotionRecord
router.register(r'emotions', EmotionRecordViewSet)

# Define os padrões de URL para esta aplicação
# router.urls contém todas as URLs geradas automaticamente pelo router
urlpatterns = router.urls

# Nota: A importação 'home_view' não está sendo usada neste arquivo.
# Se você quiser adicionar uma URL personalizada, poderia fazer:
# urlpatterns = [
#     path('minha-url/', minhaview, name='minha-view'),
# ] + router.urls
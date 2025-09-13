from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    """
    ============================================================
                    VIEW SIMPLES PARA PÁGINA INICIAL
    ============================================================
    
    Esta view retorna uma resposta HTTP básica com uma mensagem simples.
    No entanto, note que esta view NÃO está sendo usada atualmente,
    pois a página inicial está definida no arquivo principal urls.py.
    
    Para usar esta view, você precisaria mapeá-la para uma URL em
    emotions/urls.py ou dorotea_backend/urls.py.
    """
    return HttpResponse("Página inicial do Dorotea")

# Importações para a API REST
from rest_framework import viewsets
from .models import EmotionRecord
from .serializers import EmotionRecordSerializer
from rest_framework.parsers import MultiPartParser

class EmotionRecordViewSet(viewsets.ModelViewSet):
    """
    ============================================================
                VIEWSET PARA O MODELO EMOTIONRECORD
    ============================================================
    
    O que é um ViewSet?
    - É uma classe do Django REST Framework que combina a lógica
      para várias operações relacionadas em uma única classe
    - Fornece automaticamente ações CRUD (Create, Read, Update, Delete)
    - Gera automaticamente URLs quando registrado em um Router
    
    O que acontece quando alguém acessa a API?
    
    1. LISTAGEM (GET /api/emotions/)
       - Retorna todos os registros de EmotionRecord
       - Usa o serializer para converter para JSON
    
    2. CRIAÇÃO (POST /api/emotions/)
       - Recebe dados JSON ou multipart/form-data (com imagem)
       - Valida os dados usando o serializer
       - Salva no banco de dados
       - Retorna o objeto criado
    
    3. DETALHES (GET /api/emotions/{id}/)
       - Retorna um registro específico pelo ID
    
    4. ATUALIZAÇÃO (PUT/PATCH /api/emotions/{id}/)
       - Atualiza um registro existente
       - PUT substitui todo o objeto, PATCH atualiza parcialmente
    
    5. EXCLUSÃO (DELETE /api/emotions/{id}/)
       - Remove um registro do banco de dados
    
    Configurações especiais:
    - parser_classes = [MultiPartParser]: Permite upload de arquivos
      (necessário para enviar imagens através da API)
    
    ============================================================
    """
    
    # Define quais objetos estarão disponíveis (todos os EmotionRecord)
    queryset = EmotionRecord.objects.all()
    
    # Define qual serializer será usado para converter os objetos
    serializer_class = EmotionRecordSerializer
    
    # Permite que a view aceite upload de arquivos (multipart/form-data)
    parser_classes = [MultiPartParser]
    
    # Métodos personalizados que você pode adicionar no futuro:
    # def perform_create(self, serializer):
    #     """Executa ações adicionais ao criar um registro"""
    #     # Exemplo: registrar quem criou o registro
    #     instance = serializer.save()
    #     print(f"Novo registro criado: {instance.emotion}")
    #
    # def get_queryset(self):
    #     """Personaliza a consulta base"""
    #     # Exemplo: filtrar apenas registros de uma emoção específica
    #     emotion = self.request.query_params.get('emotion')
    #     if emotion:
    #         return EmotionRecord.objects.filter(emotion=emotion)
    #     return EmotionRecord.objects.all()de imagens

    # O que acontece quando alguem acessa emotions api
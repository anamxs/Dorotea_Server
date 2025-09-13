from rest_framework import serializers
from .models import EmotionRecord

class EmotionRecordSerializer(serializers.ModelSerializer):
    """
    ============================================================
                  SERIALIZER PARA O MODELO EMOTIONRECORD
    ============================================================
    
    O que é um Serializer?
    - É um componente do Django REST Framework (DRF)
    - Converte objetos Python (modelos) em formatos como JSON
    - Converte dados recebidos (JSON) de volta em objetos Python
    
    Para que serve este Serializer específico?
    - Transforma registros do banco de dados (EmotionRecord) em JSON
    - Valida dados recebidos pela API antes de salvar no banco
    - Define quais campos do modelo são expostos na API
    
    Como funciona no fluxo da aplicação?
    1. Cliente (Flutter) envia dados para a API
    2. Serializer valida e desserializa os dados
    3. Dados são salvos no banco como EmotionRecord
    4. Ao consultar dados, Serializer converte EmotionRecord para JSON
    5. JSON é retornado para o cliente
    
    ============================================================
    """
    
    class Meta:
        model = EmotionRecord  # Modelo associado a este Serializer
        
        # Campos a serem incluídos na serialização
        # '__all__' significa "todos os campos do modelo"
        fields = '__all__'
        
        # Alternativa: listar campos explicitamente (mais seguro)
        # fields = ['id', 'timestamp', 'emotion', 'image']
        
        # Opções adicionais que podem ser úteis:
        # read_only_fields = ['id', 'timestamp']  # Campos apenas leitura
        # extra_kwargs = {'image': {'required': False}}  # Tornar imagem opcional

    # Exemplo de método personalizado que você pode adicionar:
    # def get_emotion_uppercase(self, obj):
    #     """Método personalizado para retornar a emoção em maiúsculas"""
    #     return obj.emotion.upper() if obj.emotion else None
    
    # Exemplo de campo personalizado que você pode adicionar:
    # emotion_uppercase = serializers.SerializerMethodField(
    #     method_name='get_emotion_uppercase'
    # )
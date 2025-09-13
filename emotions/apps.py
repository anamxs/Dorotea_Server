from django.apps import AppConfig

class EmotionsConfig(AppConfig):
    """
    ============================================================
              CONFIGURAÇÃO DA APLICAÇÃO EMOTIONS
    ============================================================
    
    O QUE É ESTE ARQUIVO?
    - É o arquivo de configuração específico da aplicação 'emotions'
    - Define metadados e comportamentos personalizados para o app
    
    PARA QUE SERVE?
    1. Configurar o tipo de campo automático padrão para modelos
    2. Definir o nome da aplicação (deve corresponder ao nome da pasta)
    3. Permitir inicialização personalizada da aplicação
    4. Definir nome amigável para exibição (verbose_name)
    
    COMO É USADO PELO DJANGO?
    - Quando você adiciona 'emotions' em INSTALLED_APPS no settings.py
    - O Django procura por uma classe AppConfig neste arquivo
    - Usa esta configuração para gerenciar o aplicativo
    
    ============================================================
    """
    
    # Define o tipo de campo padrão para chaves primárias automáticas
    # BigAutoField é um inteiro de 64 bits (maior que AutoField de 32 bits)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nome do aplicativo (deve corresponder ao nome da pasta)
    name = 'emotions'
    
    # Nome amigável para exibição em interfaces administrativas
    # (Se quiser adicionar, descomente a linha abaixo)
    # verbose_name = "Gerenciador de Emoções"
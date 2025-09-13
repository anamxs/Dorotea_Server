from django.db import models

class EmotionRecord(models.Model):
    """
    ============================================================
                  MODELO DE DADOS EMOTIONRECORD
    ============================================================
    
    Este modelo define a estrutura da tabela no banco de dados
    que armazenará os registros de emoções detectadas pela IA.
    
    Cada instância representa um registro único com:
    - Timestamp (data/hora) da detecção
    - Emoção detectada
    - Imagem associada (opcional)
    
    O Django automaticamente cria uma tabela no banco de dados
    com base nesta definição quando as migrações são aplicadas.
    
    ============================================================
    """
    
    # Data e hora automática da criação do registro
    # auto_now_add=True define automaticamente no momento da criação
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Campo para armazenar a emoção detectada pela IA
    # CharField com max_length=50 permite até 50 caracteres
    emotion = models.CharField(max_length=50)
    
    # Campo para armazenar a imagem associada à emoção detectada
    # upload_to='frames/' especifica o diretório dentro de MEDIA_ROOT
    # null=True permite valor NULL no banco de dados
    # blank=True permite campo vazio em formulários
    image = models.ImageField(upload_to='frames/', null=True, blank=True)
    
    class Meta:
        """
        Classe Meta para configurações adicionais do modelo
        """
        # Declaração explícita do app_label (útil em projetos complexos)
        app_label = 'emotions'
        
        # Outras opções Meta que você pode adicionar futuramente:
        # verbose_name = "Registro de Emoção"  # Nome amigável singular
        # verbose_name_plural = "Registros de Emoções"  # Nome plural
        # ordering = ['-timestamp']  # Ordenação padrão (mais recente primeiro)
    
    def __str__(self):
        """
        Representação em string do objeto (para admin e shell)
        """
        return f"Emoção {self.emotion} em {self.timestamp}"
    
    # Métodos adicionais que você pode implementar no futuro:
    # def get_absolute_url(self):
    #     """Retorna a URL para acessar este registro específico"""
    #     return reverse('emotion-detail', kwargs={'pk': self.pk})
    #
    # def get_image_url(self):
    #     """Retorna a URL completa da imagem se existir"""
    #     if self.image:
    #         return self.image.url
    #     return None
"""
ASGI config for DoroTEA_Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/

============================================================
                    EXPLICAÇÃO DETALHADA
============================================================

O QUE É ESTE ARQUIVO?
- Este é o ponto de entrada para aplicações ASGI (Asynchronous Server Gateway Interface)
- É a evolução do WSGI, com suporte a operações assíncronas e protocolos modernos

PARA QUE SERVE NO PROJETO DOROTEA?
1. Permite que o servidor Django lide com conexões assíncronas
2. Habilita suporte para WebSockets (comunicação em tempo real)
3. Prepara o projeto para funcionalidades futuras como:
   - Atualizações em tempo real das emoções detectadas
   - Notificações instantâneas para o app Flutter
   - Transmissão de vídeo ao vivo

QUANDO É USADO?
- Em desenvolvimento: Quando usando servidores ASGI como Daphne ou Uvicorn
- Em produção: Para deploy com suporte a WebSockets e HTTP/2
- Para funcionalidades avançadas: Como Django Channels

COMO FUNCIONA?
1. Configura qual arquivo de settings usar (DoroTEA_Backend.settings)
2. Cria uma "application" ASGI que o servidor web usará
3. Expõe esta application para servidores ASGI externos

EXEMPLO DE USO FUTURO:
Se quisermos adicionar atualizações em tempo real:
1. Instalar: pip install channels
2. Adicionar suporte a WebSockets aqui
3. Usar servidor ASGI em produção

ATUALMENTE:
- O projeto está usando principalmente WSGI para requisições HTTP tradicionais
- Este arquivo está configurado mas não está sendo usado ativamente
- Está pronto para quando precisarmos de funcionalidades mais avançadas

============================================================
          ARQUIVO MANTIDO PARA FUTURAS EXPANSÕES
============================================================
"""

import os

from django.core.asgi import get_asgi_application

# Configura qual módulo de settings usar
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoroTEA_Backend.settings')

# Cria a aplicação ASGI que será usada por servidores ASGI
application = get_asgi_application()
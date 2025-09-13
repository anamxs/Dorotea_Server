"""
WSGI config for DoroTEA_Backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

============================================================
              CONFIGURAÇÃO WSGI DO PROJETO DOROTEA
============================================================

O QUE É WSGI?
- Web Server Gateway Interface (WSGI) é um padrão Python para servidores web
- Funciona como uma ponte entre o servidor web e sua aplicação Django
- Permite que servidores web (Apache, Nginx, Gunicorn) comuniquem com o Django

PARA QUE SERVE ESTE ARQUIVO?
- Expõe a aplicação Django como uma variável chamada "application"
- Configura qual módulo de settings deve ser usado
- É o ponto de entrada principal para servidores web em PRODUÇÃO

DIFERENÇA ENTRE WSGI E ASGI:
- WSGI: Síncrono, ideal para requisições tradicionais HTTP/HTTPS
- ASGI: Assíncrono, ideal para WebSockets e conexões de longa duração

QUANDO ESTE ARQUIVO É USADO?
- Em ambiente de PRODUÇÃO quando usando:
  * Apache + mod_wsgi
  * Nginx + Gunicorn
  * Outros servidores WSGI-compatíveis
- NÃO é usado durante desenvolvimento (quando usa-se runserver)

COMO FUNCIONA NO DOROTEA?
1. O servidor web (ex: Nginx) recebe uma requisição
2. Nginx passa a requisição para o Gunicorn (servidor WSGI)
3. Gunicorn chama este arquivo para obter a "application"
4. A "application" processa a requisição e retorna a resposta

CONFIGURAÇÃO ATUAL:
- Usa as configurações do DoroTEA_Backend.settings
- Configurado para usar o modo padrão do Django WSGI

PARA DEPLOY EM PRODUÇÃO:
1. Instale um servidor WSGI como Gunicorn: pip install gunicorn
2. Configure um servidor web como Nginx para proxy reverso
3. Use este arquivo como ponto de entrada para o Gunicorn

EXEMPLO DE USO COM GUNICORN:
gunicorn DoroTEA_Backend.wsgi:application --bind 0.0.0.0:8000

EM DESENVOLVIMENTO:
- O comando runserver usa seu próprio servidor leve
- Este arquivo não é utilizado durante desenvolvimento

============================================================
          ARQUIVO ESSENCIAL PARA DEPLOY EM PRODUÇÃO
============================================================
"""

import os

from django.core.wsgi import get_wsgi_application

# Configura qual módulo de settings o Django deve usar
# Isso diz ao Django: "Use as configurações do DoroTEA_Backend.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoroTEA_Backend.settings')

# Cria a aplicação WSGI que será usada pelos servidores web
# Esta variável "application" é o que os servidores WSGI procuram
application = get_wsgi_application()
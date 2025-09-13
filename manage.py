#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# Inicia o servidor e os comandos administrativos do Django
import os
import sys

def main():
    """Run administrative tasks."""
    # Configura qual módulo de settings será usado pelo Django
    # Isso diz ao Django: "Use as configurações do DoroTEA_Backend.settings"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DoroTEA_Backend.settings')
    
    try:
        # Tenta importar a função que executa comandos do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Se não conseguir importar, significa que o Django não está instalado
        # ou não está disponível no ambiente Python atual
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Executa o comando recebido pela linha de comando
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Este bloco garante que a função main() só seja executada
    # quando o arquivo for rodado diretamente (não quando importado)
    main()
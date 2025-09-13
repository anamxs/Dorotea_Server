import subprocess
import time
import webbrowser
import os
import sys

def start_django_server():
    """
    ============================================================
                INICIALIZADOR DO SERVIDOR DJANGO
    ============================================================
    
    Função: Inicia o servidor Django em um terminal separado
    Método: Usa PowerShell para criar uma nova janela de terminal
    Comandos executados:
      1. Navega para o diretório do projeto
      2. Ativa o ambiente virtual
      3. Executa 'python manage.py runserver'
    
    Benefícios:
      - Mantém o servidor rodando em janela separada
      - Permite ver logs e erros do Django em tempo real
      - Não bloqueia o terminal principal
    """
    # Comando para iniciar o servidor
    command = [
        "powershell",
        "-NoExit",  # Mantém o PowerShell aberto após execução
        "-Command",
        f"cd '{os.getcwd()}'; .\.venv\Scripts\Activate.ps1; python manage.py runserver"
    ]
    
    # Inicia em um novo terminal
    subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Servidor Django iniciado em novo terminal...")

def start_video_ingest():
    """
    ============================================================
                INICIALIZADOR DO SCRIPT DE INGESTÃO
    ============================================================
    
    Função: Inicia o script video_ingest.py em terminal separado
    Método: Similar ao servidor Django, mas executa o script de ingestão
    
    Benefícios:
      - Permite simulação de câmera em paralelo com o servidor
      - Mostra logs do script de ingestão em janela dedicada
      - Não interfere com o terminal principal
    """
    # Comando para iniciar o script
    command = [
        "powershell",
        "-NoExit",
        "-Command",
        f"cd '{os.getcwd()}'; .\.venv\Scripts\Activate.ps1; python video_ingest.py"
    ]
    
    # Inicia em um novo terminal
    subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Script de ingestão iniciado em novo terminal...")

def open_browser_when_ready():
    """
    ============================================================
                ABERTURA AUTOMÁTICA DO NAVEGADOR
    ============================================================
    
    Função: Aguarda o servidor ficar disponível e abre o navegador
    Método: Verifica acessibilidade do localhost antes de abrir URL
    
    Benefícios:
      - Evita erro de "página não disponível"
      - Garante que o navegador só abre quando o servidor estiver pronto
      - Melhora a experiência do usuário
    """
    print("Aguardando servidor ficar disponível...")
    url = "http://localhost:8000/api/emotions/"
    
    # Tenta acessar até conseguir
    while True:
        try:
            # Verifica se o localhost está respondendo
            response = os.system("ping -n 1 localhost > nul")
            if response == 0:
                webbrowser.open(url)
                print(f"Página aberta: {url}")
                break
        except:
            pass
        
        time.sleep(1)

if __name__ == "__main__":
    """
    ============================================================
                    PROGRAMA PRINCIPAL
    ============================================================
    
    Fluxo de execução:
      1. Inicia o servidor Django
      2. Aguarda 5 segundos para inicialização
      3. Abre o navegador automaticamente
      4. Pergunta se deve iniciar o script de ingestão
    
    Como usar:
      - Execute: python start_server.py
      - Responda 's' ou 'n' para iniciar o script de ingestão
    """
    start_django_server()
    time.sleep(5)  # Espera o servidor iniciar
    open_browser_when_ready()
    
    # Pergunta se quer iniciar o script de ingestão
    if input("\nIniciar script de ingestão também? (s/n): ").lower() == 's':
        start_video_ingest()
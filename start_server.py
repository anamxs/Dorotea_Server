import subprocess
import time
import webbrowser
import os
import sys

def start_django_server():
    """Inicia o servidor Django em um novo terminal"""
    # Comando para iniciar o servidor
    command = [
        "powershell",
        "-NoExit",
        "-Command",
        f"cd '{os.getcwd()}'; .\.venv\Scripts\Activate.ps1; python manage.py runserver"
    ]
    
    # Inicia em um novo terminal
    subprocess.Popen(command, creationflags=subprocess.CREATE_NEW_CONSOLE)
    print("Servidor Django iniciado em novo terminal...")

def start_video_ingest():
    """Inicia o script de ingestão em outro terminal"""
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
    """Abre o navegador quando o servidor estiver pronto"""
    print("Aguardando servidor ficar disponível...")
    url = "http://localhost:8000/api/emotions/"
    
    # Tenta acessar até conseguir
    while True:
        try:
            # Tenta uma conexão simples
            response = os.system(f"ping -n 1 localhost > nul")
            if response == 0:
                webbrowser.open(url)
                print(f"Página aberta: {url}")
                break
        except:
            pass
        
        time.sleep(1)

if __name__ == "__main__":
    start_django_server()
    time.sleep(5)  # Espera o servidor iniciar
    open_browser_when_ready()
    
    # Pergunta se quer iniciar o script de ingestão
    if input("\nIniciar script de ingestão também? (s/n): ").lower() == 's':
        start_video_ingest()
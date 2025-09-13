import requests
import time
import os

# Configurações
API_URL = "http://localhost:8000/api/emotions/"  # URL da API
IMAGE_PATH = r"E:\Dorotea_Server\DoroTEA_Backend\test_image.jpg"  # Caminho para a imagem de teste (coloque na mesma pasta deste script)
# Verifica se a imagem existe
if not os.path.exists(IMAGE_PATH):
    print(f"Erro: Imagem de teste não encontrada em {IMAGE_PATH}")
    print("Por favor, coloque uma imagem chamada 'test_image.jpg' na pasta do projeto.")
    exit(1)
# Loop de envio
while True:
    try:
        # Abre a imagem estatica e envia para a API
        with open(IMAGE_PATH, 'rb') as img:
            # Prepara os dados: campo 'emotion' e campo 'image'
            data = {'emotion': 'happy'}  # Emoção fixa para teste, futuramente chama IA
            files = {'image': img}  
            import cv2

            urls = [
                "rtsp://10.167.246.100:554/stream1",
                "rtsp://10.167.246.100:554/11",
                "http://10.167.246.100:80/videostream.cgi",
                "http://10.167.246.100:8080/video"
            ]

            for url in urls:
                cap = cv2.VideoCapture(url)
                if cap.isOpened():
                    print(f"Sucesso! URL: {url}")
                    break
                else:
                    print(f"Falha: {url}")
            # Futuramente
            #import cv2
            #cap = cv2.VideoCapture(0)  # 0 para a câmera padrão
            #while True:
            #ret, frame = cap.read()
            #if not ret:
            #break
            
            # Faz a requisição POST, envia para o servidor Django
            response = requests.post(API_URL, data=data, files=files)
            
            # Verifica a resposta
            if response.status_code == 201:
                print(f"Enviado com sucesso! Resposta: {response.json()}")
            else:
                print(f"Erro no servidor: {response.status_code}, Resposta: {response.text}")
    
    except Exception as e:
        print(f"Erro durante o envio: {str(e)}")
    
    # Espera 5 segundos antes de enviar novamente
    time.sleep(5)
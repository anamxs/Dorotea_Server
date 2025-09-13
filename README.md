# Servidor do Projeto DOROTEA

Este repositório contém a implementação do **servidor de ingestão de vídeo** do projeto DOROTEA, responsável por capturar imagens de uma câmera, processar as emoções detectadas e disponibilizar os dados para o aplicativo.

## Funcionalidades

- Conexão com stream RTSP da câmera.
- Captura de frames em tempo real usando OpenCV.
- Integração com o módulo de IA para detecção de emoções.
- Armazenamento de resultados no banco de dados via Django ORM (emoção + timestamp).
- Opcional: exibição do vídeo ao vivo via Django usando `StreamingHttpResponse`.

## Estrutura do projeto

- `video_ingest.py`: script responsável pela captura de vídeo e envio para processamento de IA.
- `backend_django/`: projeto Django que gerencia o banco de dados, APIs REST e integração com o app.
- `media/`: pasta para armazenar imagens temporárias ou arquivos de mídia, se necessário.

## Objetivo

Permitir que o **app DOROTEA** acesse dados de emoção das crianças em **quase tempo real**, além de manter um histórico armazenado para análises posteriores.

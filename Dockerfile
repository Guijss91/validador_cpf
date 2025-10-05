# Imagem base Python slim
FROM python:3.11-slim

# Evita buffering e pyc
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Cria diretório de trabalho
WORKDIR /app

# Copia requisitos e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY app.py .

# Expõe a porta do Flask
EXPOSE 8000

# Comando para iniciar a app
CMD ["python", "app.py"]

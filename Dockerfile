# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /biblio

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requirements para o contêiner
COPY requirements.txt requirements.txt

# Instala as dependências necessárias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do projeto para o diretório de trabalho
COPY ./biblio ./biblio

# Expõe a porta que a aplicação irá rodar
EXPOSE 8080

# Comando para rodar a aplicação usando waitress
CMD ["waitress-serve", "--host=0.0.0.0","--port=8080", "biblio:app"]

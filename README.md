Documentação do Projeto
Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados

Segue a lista de hashtags coletadas:

#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing


Pré-requisitos:




Docker 20.10.2+

Docker Compose 1.27.4+

Python 3.6.12+

PyPi (pip) 21.0.1+

Requisitos bibliotecas Python requirements.txt


Variaveis de necessárias para execução:

Variaveis de autenticação com Twitter necessário exportar:

export CONSUMER_KEY=<your-consumer-key>

export CONSUMER_SECRET=<your-consumer-secret>

export ACCESS_TOKEN=<your-access-token>

export ACCESS_TOKEN_SECRET=<your-access-token-secret>


Variaveis com informação de acesso ao mongodb:

export MONGO_SERVER=‘mongodb://mongo:27017’

export MONGO_USER=root

export MONGO_PWD=mypass

Passo a passo:

Fazer o clone da imagem do git:
git clone https://github.com/gpinotti/twitter_case.git
Criar o arquivo .env dentro do diretório twitter_case/deploy contendo as informações:

Criação do user utilizado no DB
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=mypass

Usuário de acesso ao DB
MONGO_SERVER=mongodb://mongo:27017
MONGO_USER=root
MONGO_PWD=mypass

Token autenticação Twitter
CONSUMER_KEY=
CONSUMER_SECRET=
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=

Inicializar os containers através do docker compose:
cd twitter_case/deploy
docker-compose -f docker-compose.yml up -d

Script de coleta do Twitter e escrita no db:

collect_tweets.py

Script que lista os 5 usuarios com maior numero de seguidoresna base:

rank_users.py


Total de postagem alocadas por hora do dia:

count_tweets_by_hour.py


O total de postagens para cada uma das hashtags por idioma:



Referencias:


Linguagem: Python 3

Lib API Twitter: Tweepy

Framework APIs: Flask

Monitoramento: Prometheus

Logs:

Elasticsearch

Filebeat

Kibana

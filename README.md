**Documentação do Projeto**

Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados

Segue a lista de hashtags coletadas:
*#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing*

**Pré-requisitos**:
```
*Docker 20.10.2+*
*Docker Compose 1.27.4+*
*Python 3.6.12+*
*PyPi (pip) 21.0.1+*
```
Requisitos bibliotecas Python [requirements.txt](src/requirements.txt)
###########################################

1 - Script que busca os Tweets e popula o mongodb:

[collect_tweets.py](src/collect_tweets.py)

2 - Script que lista os 5 usuarios com maior numero de seguidoresna base:

[rank_users.py](src/rank_users.py)

3 - Total de postagem alocadas por hora do dia:

[count_tweets_by_hour.py](src/count_tweets_by_hour.py)

4 - O total de postagens para cada uma das hashtags por idioma:


Para execução em um ambiente local é necessário exportar as variáveis listadas abaixo.

Variáveis de autenticação com Twitter necessário exportar no sistema operacional:

```
export CONSUMER_KEY=***<your-consumer-key>***
export CONSUMER_SECRET=***<your-consumer-secret>***
export ACCESS_TOKEN=***<your-access-token>***
export ACCESS_TOKEN_SECRET=***<your-access-secret>***
```

Variáveis com informação de acesso ao mongodb:

```
export MONGO_SERVER=‘mongodb://mongo:27017’
export MONGO_USER=root
export MONGO_PWD=mypass
```

#####################################################

**Execução ambiente docker**

Clone do repositório git:

```
git clone https://github.com/gpinotti/twitter_case.git
```

Criar o arquivo .env dentro do diretório twitter_case/deploy contendo as informações:

```
#Usuário e Senha que será criado na inicialização do mongodb
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=mypass

##Usuário e senha utilizados no acesso do mongodb
MONGO_SERVER=mongodb://mongo:27017
MONGO_USER=root
MONGO_PWD=mypass

##Token autenticação Twitter
CONSUMER_KEY=***<your-consumer-key>***
CONSUMER_SECRET=***<your-consumer-secret>***
ACCESS_TOKEN=***<your-access-token>***
ACCESS_TOKEN_SECRET=***<your-access-secret>***
```

Inicializar os containers através do docker-compose:

```
cd twitter_case/deploy
docker-compose -f docker-compose.yml up -d
```
Desligar a aplicação via docker compose:

```
docker-compose -f docker-compose.yml down
```

**Informações de acessos as APIs:**

URL local [http://localhost:8081](http://localhost:8081/)

| **rotas**              | **metodos** | **ResponseCode: "Success"** | **ResponseCode: "Failure"** | **descricao**                                                |
| ---------------------- | ----------- | --------------------------- | --------------------------- | ------------------------------------------------------------ |
| /api/tweets            | `GET`       | `200`                       | `500`                       | Retorna a lista completa dos tweets carregados pelo loader e salvos no banco de dados. |
| /api/rank-by-followers | `GET`       | `200`                       | `500`                       | Retorna o top 5 usuarios com mais seguidores salvos no BD.   |
| /api/tweets-per-hour   | `GET`       | `200`                       | `500                        | Total de tweets por hora do dia salvos no BD                 |
| /api/reload-tweets     | `POST`      | `201`                       | `503`                       | Carrega uma nova lista de tweets e salva no BD               |

**Monitoramento / LOGS**

Acesso ao grafana:

http://localhost:3000

```
User: admin
Senha: admin
```



**Print dashboard:**

![](/images/Graphana.PNG)



**Coleção no postman para consumir as APIs**

[twitter-case.postman_collection.json](postman/twitter-case.postman_collection.json)

"How to" de como importar:

https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-via-github-repositories




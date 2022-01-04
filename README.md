# twitter_case
##### Documentação do Projeto

Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados
Segue a lista de hashtags coletadas:
#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing

Pré-requisitos:
Docker 20.10.2+
Docker Compose 1.27.4+
Python 3.6.12+
PyPi (pip) 21.0.1+
Requisitos bibliotecas Python [requirements.txt](src/requirements.txt)

##### Variaveis de necessárias para execução:


Variaveis de autenticação com Twitter necessário exportar:
export CONSUMER_KEY=<your-consumer-key>
export CONSUMER_SECRET=<your-consumer-secret>
export ACCESS_TOKEN=<your-access-token>
export ACCESS_TOKEN_SECRET=<your-access-token-secret>

Variaveis com informação de acesso ao mongodb:
export MONGO_SERVER='mongodb://mongo:27017'
export MONGO_USER=root
export MONGO_PWD=mypass

1. Script  de coleta do Twitter e escrita no db:
[collect_tweets.py](src/collect_tweets.py)


2. Script que lista os 5 usuarios com maior numero de seguidoresna base:
[rank_users.py](src/rank_users.py)

3. Total de postagem alocadas por hora do dia:
[count_tweets_by_hour.py](src/count_tweets_by_hour.py)

4. O total de postagens para cada uma das hashtags por idioma:


Referencias:

- Linguagem: [Python 3](https://www.python.org/)
- Lib API Twitter: [Tweepy](https://www.tweepy.org/)
- Framework APIs: [Flask](https://palletsprojects.com/p/flask/)
- Monitoramento: [Prometheus](https://prometheus.io/)
- Logs:
    - [Elasticsearch](https://www.elastic.co/pt/elasticsearch/)
    - [Filebeat](https://www.elastic.co/pt/beats/filebeat)
    - [Kibana](https://www.elastic.co/pt/kibana)

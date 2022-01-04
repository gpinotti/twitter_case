# twitter_case
Documentação do Projeto

Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados
Segue a lista de hashtags coletadas:
#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing

Pré-requisitos:

Requisitos:
Docker 20.10.2+
Docker Compose 1.27.4+
Python 3.6.12+
PyPi (pip) 21.0.1+

- Demais requisitos no arquivo [requirements.txt](twitter_case/src/requirements.txt)

1. Script  de coleta do Twitter e escrita no db:
https://github.com/gpinotti/twitter_case/blob/main/src/collect_tweets.py


2. Script que lista os 5 usuarios com maior numero de seguidoresna base:
https://github.com/gpinotti/twitter_case/blob/main/src/rank_users.py

3. Total de postagem alocadas por hora do dia:
https://github.com/gpinotti/twitter_case/blob/main/src/count_tweets_by_hour.py

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

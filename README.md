# twitter_case
Documentação do Projeto
Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados
Segue a lista de hashtags coletadas:
#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing




1. Dentre os usuários dos tweets buscados, os 5 (cinco) que possuem mais seguidores; :white_check_mark:
2. O total de postagens, agrupadas por hora do dia (independentemente da hashtag); :white_check_mark:
3. O total de postagens para cada uma das hashtags por idioma/país do usuário que postou :x:

Para inicialização rapida do projeto, executar o [quick-start](#quick-start)
<br>

-----

A stack consiste das seguintes tecnologias:

- Linguagem: [Python 3](https://www.python.org/)
- Lib API Twitter: [Tweepy](https://www.tweepy.org/)
- Framework APIs: [Flask](https://palletsprojects.com/p/flask/)
- Monitoramento: [Prometheus](https://prometheus.io/)
- Logs:
    - [Elasticsearch](https://www.elastic.co/pt/elasticsearch/)
    - [Filebeat](https://www.elastic.co/pt/beats/filebeat)
    - [Kibana](https://www.elastic.co/pt/kibana)
<br>


-----
## <a name=quick-start></a>Quick Start
<br>

#### Requisitos:

- [Docker](https://www.docker.com/products/docker-desktop) 20.10.2+
- [Docker Compose](https://docs.docker.com/compose/install/) 1.27.4+


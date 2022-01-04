<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="twitter_case_0"></a>twitter_case</h1>
<h5 class="code-line" data-line-start=1 data-line-end=2 ><a id="Documentao_do_Projeto_1"></a>Documentação do Projeto</h5>
<p class="has-line-data" data-line-start="3" data-line-end="6">Este projeto coleta dados do Twitter que contenham algumas hashtags pré-definidas e armazena em banco de dados<br>
Segue a lista de hashtags coletadas:<br>
#devops, #sre, #microservices, #observability, #oauth, #metrics, #logmonitoring, #opentracing</p>
<p class="has-line-data" data-line-start="7" data-line-end="13">Pré-requisitos:<br>
Docker 20.10.2+<br>
Docker Compose 1.27.4+<br>
Python 3.6.12+<br>
PyPi (pip) 21.0.1+<br>
Requisitos bibliotecas Python <a href="src/requirements.txt">requirements.txt</a></p>
<h5 class="code-line" data-line-start=14 data-line-end=15 ><a id="Variaveis_de_necessrias_para_execuo_14"></a>Variaveis de necessárias para execução:</h5>
<p class="has-line-data" data-line-start="17" data-line-end="22">Variaveis de autenticação com Twitter necessário exportar:<br>
export CONSUMER_KEY=&lt;your-consumer-key&gt;<br>
export CONSUMER_SECRET=&lt;your-consumer-secret&gt;<br>
export ACCESS_TOKEN=&lt;your-access-token&gt;<br>
export ACCESS_TOKEN_SECRET=&lt;your-access-token-secret&gt;</p>
<p class="has-line-data" data-line-start="23" data-line-end="27">Variaveis com informação de acesso ao mongodb:<br>
export MONGO_SERVER=‘mongodb://mongo:27017’<br>
export MONGO_USER=root<br>
export MONGO_PWD=mypass</p>

**Passo a passo:**
- Fazer o clone da imagem do git:
git clone https://github.com/gpinotti/twitter_case.git

- Criar o arquivo .env dentro do diretório twitter_case/deploy contendo as informações:
####Criação do user utilizado no DB
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=mypass
####Usuário de acesso ao DB
MONGO_SERVER=mongodb://mongo:27017
MONGO_USER=root
MONGO_PWD=mypass
####Token autenticação Twitter
CONSUMER_KEY=<your key>
CONSUMER_SECRET=<your key>
ACCESS_TOKEN=<your key>
ACCESS_TOKEN_SECRET=<your key>

- Inicializar os containers através do docker compose:
cd twitter_case/deploy
docker-compose -f docker-compose.yml up -d
<ol>
<li class="has-line-data" data-line-start="28" data-line-end="30">Script  de coleta do Twitter e escrita no db:<br>
<a href="src/collect_tweets.py">collect_tweets.py</a></li>
</ol>
<ol start="2">
<li class="has-line-data" data-line-start="32" data-line-end="35">
<p class="has-line-data" data-line-start="32" data-line-end="34">Script que lista os 5 usuarios com maior numero de seguidoresna base:<br>
<a href="src/rank_users.py">rank_users.py</a></p>
</li>
<li class="has-line-data" data-line-start="35" data-line-end="38">
<p class="has-line-data" data-line-start="35" data-line-end="37">Total de postagem alocadas por hora do dia:<br>
<a href="src/count_tweets_by_hour.py">count_tweets_by_hour.py</a></p>
</li>
<li class="has-line-data" data-line-start="38" data-line-end="39">
<p class="has-line-data" data-line-start="38" data-line-end="39">O total de postagens para cada uma das hashtags por idioma:</p>
</li>
</ol>
<p class="has-line-data" data-line-start="41" data-line-end="42">Referencias:</p>
<ul>
<li class="has-line-data" data-line-start="43" data-line-end="44">Linguagem: <a href="https://www.python.org/">Python 3</a></li>
<li class="has-line-data" data-line-start="44" data-line-end="45">Lib API Twitter: <a href="https://www.tweepy.org/">Tweepy</a></li>
<li class="has-line-data" data-line-start="45" data-line-end="46">Framework APIs: <a href="https://palletsprojects.com/p/flask/">Flask</a></li>
<li class="has-line-data" data-line-start="46" data-line-end="47">Monitoramento: <a href="https://prometheus.io/">Prometheus</a></li>
<li class="has-line-data" data-line-start="47" data-line-end="51">Logs:
<ul>
<li class="has-line-data" data-line-start="48" data-line-end="49"><a href="https://www.elastic.co/pt/elasticsearch/">Elasticsearch</a></li>
<li class="has-line-data" data-line-start="49" data-line-end="50"><a href="https://www.elastic.co/pt/beats/filebeat">Filebeat</a></li>
<li class="has-line-data" data-line-start="50" data-line-end="51"><a href="https://www.elastic.co/pt/kibana">Kibana</a></li>
</ul>
</li>
</ul>

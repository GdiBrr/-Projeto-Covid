Trabalho sobre Coronavirus.

Materia Desenvolvimento rapido de aplicação em Python:

Professor e orientador: Luiz Gustavo Turatti.

Grupo Covid19.

Particimpantes:

o	JOÃO LUCAS LAS CASAS - 202208700471
o	MARCELO JERONIMO DE OLIVEIRA - 202209188676
o	VINIICIUS MASTRANGELO DIAS - 202208700438
o	MATHEUS GIRARDI DE OLIVEIRA – 202208700462
o	Eduardo de Godoi Tasselli - 202208700314


O projeto desenvolvido é a criação de um dashboard mostrando como o Brasil foi afetado em certo período pelo coronavírus. Para fazer o Dashboard, utilizamos soluções rápidas em Python. 
A fonte de dados que utilizamos foi um arquivo CSV que conseguimos encontrar no Site Coronavírus Brasil (https://covid.saude.gov.br/).
O projeto mostra dois gráficos: um gráfico de linhas, nele conseguimos ver casos acumulados, casos novos, óbitos totais e óbitos por dia. E o outro gráfico é o mapa do Brasil, 
que mostra como cada região foi afetada pelo coronavírus, e também conseguimos selecionar uma data específica para ver os dados.

Utilizamos as seguintes bibliotecas:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, ClientsideFunction
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from import_sqlite3 import banco 
import numpy as np
import pandas as pd
import json

Componentes Dash e Dash : usados ​​para construir a interface web interativa do aplicativo.
Componentes Dash Bootstrap : usados ​​para estilizar o aplicativo e torná-lo responsivo.
Plotly : usado para criar visualizações interativas.
NumPy e Pandas : Usados ​​para manipulação de dados e operações numéricas.
SQLite : usado para operações de banco de dados para armazenar e recuperar dados.
JSON : Usado para lidar com formatos de dados JSON, que podem ser úteis para configuração ou intercâmbio de dados.

Para rodar o codigo é necessario baixar todos os arquivos disponibilizados pelo nosso grupo.

import sqlite3
import pandas as pd

class banco:
    def __init__(self):
        self.conn = sqlite3.connect('covid19.db')
        self.cursor = self.conn.cursor()

    def inserir_dado(self):


        # Cria uma tabela para os dados dos estados
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dados_estados (
                            regiao TEXT,
                            estado TEXT,
                            municipio TEXT,
                            coduf INTEGER,
                            codmun INTEGER,
                            codRegiaoSaude INTEGER,
                            nomeRegiaoSaude TEXT,
                            data DATE,
                            semanaEpi INTEGER,
                            populacaoTCU2019 INTEGER,
                            casosAcumulado INTEGER,
                            casosNovos INTEGER,
                            obitosAcumulado INTEGER,
                            obitosNovos INTEGER,
                            RecuperadosNovos INTEGER,
                            emAcompanhamentoNovos INTEGER,
                            interiorMetropolitana TEXT
                        )''')

        # Lê o arquivo CSV dos estados e insere os dados na tabela
        df_states = pd.read_csv("df_states.csv")

        df_states.to_sql('dados_estados', self.conn, if_exists='replace', index=False)

        # Cria uma tabela para os dados do Brasil
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS dados_brasil (
                            regiao TEXT,
                            estado TEXT,
                            municipio TEXT,
                            coduf INTEGER,
                            codmun INTEGER,
                            codRegiaoSaude INTEGER,
                            nomeRegiaoSaude TEXT,
                            data DATE,
                            semanaEpi INTEGER,
                            populacaoTCU2019 INTEGER,
                            casosAcumulado INTEGER,
                            casosNovos INTEGER,
                            obitosAcumulado INTEGER,
                            obitosNovos INTEGER,
                            RecuperadosNovos INTEGER,
                            emAcompanhamentoNovos INTEGER,
                            interiorMetropolitana TEXT
                        )''')

        # Lê o arquivo CSV do Brasil e insere os dados na tabela
        df_brasil = pd.read_csv("df_brasil.csv")
        df_brasil.to_sql('dados_brasil',self.conn, if_exists='replace', index=False)

   
        self.conn.commit()
        
        # Fecha a conexão

    def get_dados_brasil(self):
        query = "select * from dados_brasil"
        return pd.read_sql_query(query, self.conn) 
    def get_dados_estados(self):
        query = "select * from dados_estados"
        return pd.read_sql_query(query, self.conn) 
    
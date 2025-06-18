import pandas as pd
import plotly.express as px  # Changed this line
import streamlit as st

# LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/refs/heads/master/cases-brazil-states.csv')

# Melhorando nome de colunas na tabela
df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

# Seleção do Estado
state = 'MA'
estados = list(df['state'].unique())

# Seleção da coluna
column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']

# Seleção das linhas que pertencem ao estado
df = df[df['state'] == state]

fig = px.line(df, x='date', y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

print('DADOS COVID19 - BRASIL')
print('Nessa aplicação o usuário pode selecionar o estado e o tipo de informação para ser exibida.')

fig.show()
print('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
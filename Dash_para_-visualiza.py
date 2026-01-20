import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# --- PASSO 1: Carregar os dados ---
# Certifique-se de que o arquivo está na mesma pasta do script
try:
    df = pd.read_csv('ecommerce_estatistica.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'ecommerce_estatistica.csv' não foi encontrado na pasta.")
    # Criando dados fictícios apenas para o código não travar se o arquivo sumir
    df = pd.DataFrame({"Gênero": ["A", "B"], "Preço": [10, 20], "Nota": [5, 4]})

# --- PASSO 2: Iniciar a Aplicação ---
# Note os DOIS sublinhados: _name_
app = dash.Dash(__name__)

# --- PASSO 3: Layout ---
app.layout = html.Div([
    html.H1("Dashboard de E-commerce"),
    dcc.Dropdown(
        id='filtro-grafico',
        options=[
            {'label': 'Vendas por Gênero', 'value': 'bar'},
            {'label': 'Distribuição de Preço', 'value': 'hist'}
        ],
        value='bar'
    ),
    dcc.Graph(id='grafico-saida')
])

# --- PASSO 4: Callback (Lógica) ---
@app.callback(
    Output('grafico-saida', 'figure'),
    Input('filtro-grafico', 'value')
)
def update_graph(selection):
    if selection == 'bar':
        return px.bar(df, x='Gênero', title="Vendas por Gênero")
    else:
        return px.histogram(df, x='Preço', title="Distribuição de Preços")

# --- PASSO 5: Execução ---
# ATENÇÃO: Verifique os DOIS sublinhados abaixo
if __name__ == '_main_':
    app.run_server(debug=True)
import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash.dash_table.Format import Group
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from app import app
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
        html.Legend("Tabela de Despesas"),
        html.Div(id="table-expenses", className="dbc"),
    ]),
    dbc.Row([
            html.Legend("Tabela de Receitas"),
            html.Div(id="table-receipts", className="dbc"),
            ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Despesas"),
                    html.Legend("R$ -", id="value_expense_card",
                                style={'font-size': '60px'}),
                    html.H6("Total de despesas"),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Receitas"),
                    html.Legend("R$ +", id="value_receipt_card",
                                style={'font-size': '60px'}),
                    html.H6("Total de receitas"),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),
    dbc.Row([
            dbc.Col([
                dcc.Graph(id='bar-graph', style={"margin-right": "20px"}),
            ], width=9),
            dbc.Col([
                dcc.Graph(id='bar-graph-receipt',
                          style={"margin-right": "20px"}),
            ], width=9),
            ]),
], style={"padding": "10px"})


# =========  Callbacks  =========== #
# table


@app.callback(
    Output('table-expenses', 'children'),
    Input('store-expenses', 'data')
)
def imprimir_table(data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    table = dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": False,
                "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="single",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
    ),

    return table

# Bar Graph


@app.callback(
    Output('bar-graph', 'figure'),
    [Input('store-expenses', 'data'),
     Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria',
                   y='Valor', title="Despesas Gerais")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card


@app.callback(
    Output('value_expense_card', 'children'),
    Input('store-expenses', 'data')
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = df['Valor'].sum()

    return f"R$ {valor}"


# table receipt

@app.callback(
    Output('table-receipts', 'children'),
    Input('store-receipts', 'data')
)
def imprimir_table(data):
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data']).dt.date

    df.loc[df['Efetuado'] == 0, 'Efetuado'] = 'Não'
    df.loc[df['Efetuado'] == 1, 'Efetuado'] = 'Sim'

    df.loc[df['Fixo'] == 0, 'Fixo'] = 'Não'
    df.loc[df['Fixo'] == 1, 'Fixo'] = 'Sim'

    df = df.fillna('-')

    df.sort_values(by='Data', ascending=False)

    table = dash_table.DataTable(
        id='datatable-interactivity-2',
        columns=[
            {"name": i, "id": i, "deletable": False,
                "selectable": False, "hideable": True}
            if i == "Descrição" or i == "Fixo" or i == "Efetuado"
            else {"name": i, "id": i, "deletable": False, "selectable": False}
            for i in df.columns
        ],

        data=df.to_dict('records'),
        filter_action="native",
        sort_action="native",
        sort_mode="single",
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current=0,
        page_size=10,
    ),

    return table

# Bar Graph


@app.callback(
    Output('bar-graph-receipt', 'figure'),
    [Input('store-receipts', 'data'),
     Input(ThemeChangerAIO.ids.radio("theme"), "value")]
)
def bar_chart(data, theme):
    df = pd.DataFrame(data)
    df_grouped = df.groupby("Categoria").sum()[["Valor"]].reset_index()
    graph = px.bar(df_grouped, x='Categoria',
                   y='Valor', title="Receitas Gerais")
    graph.update_layout(template=template_from_url(theme))
    graph.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)')
    return graph

# Simple card


@app.callback(
    Output('value_receipt_card', 'children'),
    Input('store-receipts', 'data')
)
def display_desp(data):
    df = pd.DataFrame(data)
    valor = df['Valor'].sum()

    return f"R$ {valor}"

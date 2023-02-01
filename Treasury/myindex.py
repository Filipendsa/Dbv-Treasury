from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, dashboards, extracts

# DataFrames and Dcc.Store

df_receipts = pd.read_csv("df_receipts.csv", index_col=0, parse_dates=True)
df_receipts_aux = df_receipts.to_dict()

df_expenses = pd.read_csv("df_expenses.csv", index_col=0, parse_dates=True)
df_expenses_aux = df_expenses.to_dict()

list_receipts = pd.read_csv('df_cat_receipt.csv', index_col=0)
list_receipts_aux = list_receipts.to_dict()

list_expenses = pd.read_csv('df_cat_expense.csv', index_col=0)
list_expenses_aux = list_expenses.to_dict()
list_patfinder = pd.read_csv('df_dbv_patfinder.csv', index_col=0)
list_patfinder_aux = list_patfinder.to_dict()

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receipts', data=df_receipts_aux),
    dcc.Store(id="store-expenses", data=df_expenses_aux),
    dcc.Store(id='stored-cat-receipts', data=list_receipts_aux),
    dcc.Store(id='stored-cat-expenses', data=list_expenses_aux),
    dcc.Store(id='stored-dbv-ptfinder', data=list_patfinder_aux),

    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2),

        dbc.Col([
            html.Div(id="page-content")
        ], md=10),
    ])

], fluid=True, style={"padding": "0px"}, className="dbc")


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    if pathname == "/extratos":
        return extracts.layout


if __name__ == '__main__':
    app.run_server(debug=True)

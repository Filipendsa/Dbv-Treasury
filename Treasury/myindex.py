from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *

from components import sidebar, dashboards, extratos

# DataFrames and Dcc.Store

df_receipt = pd.read_csv("df_receipt.csv", index_col=0, parse_dates=True)
df_receipt_aux = df_receipt.to_dict()

df_expense = pd.read_csv("df_expense.csv", index_col=0, parse_dates=True)
df_expense_aux = df_expense.to_dict()


list_receipts = pd.read_csv('df_cat_receipt.csv', index_col=0)
list_receipts_aux = list_receipts.to_dict()

list_expense = pd.read_csv('df_cat_expense.csv', index_col=0)
list_expense_aux = list_expense.to_dict()

list_patfinder = pd.read_csv('df_dbv_patfinder.csv', index_col=0)
list_patfinder_aux = list_patfinder.to_dict()

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2),
        dbc.Col([
            content
        ], md=10)
    ])

], fluid=True,)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboards":
        return dashboards.layout

    if pathname == "/extratos":
        return extratos.layout


if __name__ == '__main__':
    app.run_server(debug=True)

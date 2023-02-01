
import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from datetime import datetime, date

import pdb
from dash_bootstrap_templates import ThemeChangerAIO

# ========= DataFrames ========= #
import numpy as np
import pandas as pd
from globals import *


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Dbv - Tesouraria", className="text-primary"),
    html.P("By FilipeNdsa", className="text-info"),
    html.Hr(),

    # ========= profile ========= #
    dbc.Button(id='button_avatar',
               children=[html.Img(src='assets/img_hom.png', id='avatar_change', alt='Avatar', className='profile_avatar')
                         ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # ========= New ========= #
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-new-receipt',
                       children=['+ receipt'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-new-expense',
                       children=['- expense'])
        ], width=6)
    ]),
    # ========= Modal receipt ========= #
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar receipt')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(
                        placeholder="Ex: Campori, inscrição, doações...", id="txt-receipt"),
                ], width=6),
                dbc.Col([
                    dbc.Label('Valor: '),
                    dbc.Input(
                        placeholder="Ex: R$100,00", id="value_receipt", value=""),
                ], width=6),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-receipt',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                                         ),
                ]),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[{"label": "Foi recebida", "value": 1},
                                 {"label": "receipt Recorrente", "value": 2}],
                        value=[1],
                        id="switches-input-receipt",
                        switch=True),
                ], width=5),
            ], style={"margin-top": "25px"}),
            dbc.Row([
                    dbc.Col([
                        html.Label("Categoria da receipt"),
                        dbc.Select(id="select_receipt", options=[
                                   {"label": i, "value": i} for i in cat_receipt], value=cat_receipt[0])
                    ], width=6),
                    dbc.Col([
                        html.Label("Desbravador"),
                        dbc.Select(id="select_patfinder", options=[
                                   {"label": i, "value": i} for i in dbv_patfinder], value=dbv_patfinder[0])
                    ], width=6)
                    ], style={"margin-top": "25px"}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar categoria", style={
                                    'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="Nova categoria...", id="input-add-receipt", value=""),
                                html.Br(),
                                dbc.Button(
                                    "Adicionar", className="btn btn-success", id="add-category-receipt", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-receipt", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Excluir categorias", style={
                                    'color': 'red'}),
                                dbc.Checklist(
                                    id="checklist-selected-style-receipt",
                                    options=[{"label": i, "value": i}
                                             for i in cat_receipt],
                                    value=[],
                                    label_checked_style={
                                        "color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button(
                                    "Remover", color="warning", id="remove-category-receipt", style={"margin-top": "20px"}),
                            ], width=6)
                        ]),
                    ], title="Adicionar/Remover Categorias",),
                ], flush=True, start_collapsed=True, id='accordion-receipt'),
            ], style={"margin-top": "25px"}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar Desbravador", style={
                                    'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="Nome Desbravador...", id="input-add-patfinder-receipt", value=""),
                                html.Br(),
                                dbc.Button(
                                    "Adicionar", className="btn btn-success", id="add-category-patfinder-receipt", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-patfinder-receipt", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Excluir desbravadores", style={
                                    'color': 'red'}),
                                dbc.Checklist(
                                    id="checklist-selected-style-patfinder-receipt",
                                    options=[{"label": i, "value": i}
                                             for i in dbv_patfinder],
                                    value=[],
                                    label_checked_style={
                                        "color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button(
                                    "Remover", color="warning", id="remove-patfinder-receipt", style={"margin-top": "20px"}),
                            ], width=6)
                        ]),
                    ], title="Adicionar/Remover Desbravadores",
                    ),
                ], flush=True, start_collapsed=True, id='accordion-patfinder-receipt'),

                html.Div(id="id_teste_receipt", style={"padding-top": "20px"}),

                dbc.ModalFooter([
                    dbc.Button(
                        "Adicionar receipt", id="save_receipt", color="success"),
                    dbc.Popover(dbc.PopoverBody(
                        "receipt Salva"), target="save_receipt", placement="left", trigger="click"),
                ])
            ], style={"margin-top": "25px"}),
        ])
    ], style={"background-color": "rgba(0, 0, 0, 0.5)"},
        id='modal-new-receipt',
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True
    ),

    # ========= Modal expense ========= #
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar expense')),
        dbc.ModalBody([
            dbc.Row([
                dbc.Col([
                    dbc.Label('Descrição: '),
                    dbc.Input(
                        placeholder="Ex: Campori, comida, brindes...", id="txt-expense"),
                ], width=6),
                dbc.Col([
                    dbc.Label('Valor: '),
                    dbc.Input(
                        placeholder="Ex: R$100,00", id="value_expense", value=""),
                ], width=6),
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-expense',
                                         min_date_allowed=date(2020, 1, 1),
                                         max_date_allowed=date(2030, 12, 31),
                                         date=datetime.today(),
                                         style={"width": "100%"}
                                         ),
                ]),
                dbc.Col([
                    dbc.Label("Extras"),
                    dbc.Checklist(
                        options=[{"label": "Foi recebida", "value": 1},
                                 {"label": "expense Recorrente", "value": 2}],
                        value=[1],
                        id="switches-input-expense",
                        switch=True),
                ], width=5),
            ], style={"margin-top": "25px"}),
            dbc.Row([
                    dbc.Col([
                        html.Label("Categoria da expense"),
                        dbc.Select(id="select_expense", options=[
                                   {"label": i, "value": i} for i in cat_expense], value=[cat_expense[0]])
                    ], width=6),
                    dbc.Col([
                        html.Label("Desbravador"),
                        dbc.Select(id="select_patfinder_expense",
                                   options=[{"label": i, "value": i} for i in dbv_patfinder], value=[dbv_patfinder[0]])
                    ], width=6)
                    ], style={"margin-top": "25px"}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar expense", style={
                                    'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="Nova categoria...", id="input-add-expense", value=""),
                                html.Br(),
                                dbc.Button(
                                    "Adicionar", className="btn btn-success", id="add-category-expense", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-expense", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Excluir categorias", style={
                                    'color': 'red'}),
                                dbc.Checklist(
                                    id="checklist-selected-style-expense",
                                    options=[{"label": i, "value": i}
                                             for i in cat_expense],
                                    value=[],
                                    label_checked_style={
                                        "color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button(
                                    "Remover", color="warning", id="remove-category-expense", style={"margin-top": "20px"}),
                            ], width=6)
                        ]),
                    ], title="Adicionar/Remover Categorias",),
                ], flush=True, start_collapsed=True, id='accordion-expense'),
            ], style={"margin-top": "25px"}),
            dbc.Row([
                dbc.Accordion([
                    dbc.AccordionItem(children=[
                        dbc.Row([
                            dbc.Col([
                                html.Legend("Adicionar Desbravador", style={
                                    'color': 'green'}),
                                dbc.Input(
                                    type="text", placeholder="Nome Desbravador...", id="input-add-patfinder-expense", value=""),
                                html.Br(),
                                dbc.Button(
                                    "Adicionar", className="btn btn-success", id="add-category-patfinder-expense", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-patfinder-expense", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Excluir desbravadores", style={
                                    'color': 'red'}),
                                dbc.Checklist(
                                    id="checklist-selected-style-patfinder-expense",
                                    options=[{"label": i, "value": i}
                                             for i in dbv_patfinder],
                                    value=[],
                                    label_checked_style={
                                        "color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button(
                                    "Remover", color="warning", id="remove-patfinder-expense", style={"margin-top": "20px"}),
                            ], width=6)
                        ]),
                    ], title="Adicionar/Remover Desbravadores",
                    ),
                ], flush=True, start_collapsed=True, id='accordion-patfinder-expense'),

                html.Div(id="id_teste_expense", style={"padding-top": "20px"}),

                dbc.ModalFooter([
                    dbc.Button(
                        "Adicionar expense", id="save_expense", color="success"),
                    dbc.Popover(dbc.PopoverBody(
                        "expense Salva"), target="save_expense", placement="left", trigger="click"),
                ])
            ], style={"margin-top": "25px"}),
        ])
    ], style={"background-color": "rgba(0, 0, 0, 0.5)"},
        id='modal-new-expense',
        size="lg",
        is_open=False,
        centered=True,
        backdrop=True
    ),
    # ========= Nav ========= #
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extratos", active="exact"),
    ], vertical=True, pills=True, id='nav_buttons', style={'margin-bottom': '50px'}),
], id='sidebar_completed')


# =========  Callbacks  =========== #
# Pop-up receipt
@app.callback(
    Output('modal-new-receipt', 'is_open'),
    Input('open-new-receipt', 'n_clicks'),
    State('modal-new-receipt', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

 # Pop-up expense


@app.callback(
    Output('modal-new-expense', 'is_open'),
    Input('open-new-expense', 'n_clicks'),
    State('modal-new-expense', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# # Pop-up perfis
# @app.callback(
#     Output("modal-profile", "is_open"),
#     Input("botao_avatar", "n_clicks"),
#     State("modal-profile", "is_open")
# )
# def toggle_modal(n1, is_open):
#     if n1:
#         return not is_open

# Enviar Form receipt


@app.callback(
    Output('store-receipt', 'data'),
    Input("save_receipt", "n_clicks"),
    [
        State("txt-receipt", "value"),
        State("value_receipt", "value"),
        State("date-receipt", "date"),
        State("switches-input-receipt", "value"),
        State("select_receipt", "value"),
        State("select_patfinder", "value"),
        State('store-receipt', 'data')
    ]
)
def save_form_receipt(n, descricao, valor, date, switches, categoria, desbravador, dict_receipt):
    df_receipt = pd.DataFrame(dict_receipt)

    if n and not (valor == "" or valor == None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria
        desbravador = desbravador[0] if type(
            desbravador) == list else desbravador

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_receipt.loc[df_receipt.shape[0]] = [
            valor, recebido, fixo, date, categoria, desbravador, descricao]
        df_receipt.to_csv("df_receipt.csv")

    data_return = df_receipt.to_dict()
    return data_return


# Enviar Form expense
@app.callback(
    Output('store-expense', 'data'),
    Input("save_expense", "n_clicks"),
    [
        State("value_expense", "value"),
        State("switches-input-expense", "value"),
        State("select_expense", "value"),
        State("select_patfinder_expense", "value"),
        State("date-expense", "date"),
        State("txt-expense", "value"),
        State('store-expense', 'data')
    ])
def save_form_expense(n, valor, switches, descricao, date, txt, desbravador, dict_expense):
    df_expense = pd.DataFrame(dict_expense)

    if n and not (valor == "" or valor == None):
        valor = round(valor, 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        if descricao == None or descricao == "":
            descricao = 0

        df_expense.loc[df_expense.shape[0]] = [
            valor, recebido, fixo, date, descricao, desbravador, txt]
        df_expense.to_csv("df_expense.csv")

    data_return = df_expense.to_dict()
    return data_return

# Add/Remove categoria expense


@app.callback(
    [Output("category-div-add-expense", "children"),
     Output("category-div-add-expense", "style"),
     Output("select_expense", "options"),
     Output('checklist-selected-style-expense', 'options'),
     Output('checklist-selected-style-expense', 'value'),
     Output('stored-cat-expense', 'data')],
    [Input("add-category-expense", "n_clicks"),
     Input("remove-category-expense", 'n_clicks')],
    [State("input-add-expense", "value"),
     State('checklist-selected-style-expense', 'value'),
     State('stored-cat-expense', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_expense = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_expense = cat_expense + \
                [txt] if txt not in cat_expense else cat_expense
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}

    if n2:
        if len(check_delete) > 0:
            cat_expense = [i for i in cat_expense if i not in check_delete]

    opt_expense = [{"label": i, "value": i} for i in cat_expense]
    df_cat_expense = pd.DataFrame(cat_expense, columns=['Categoria'])
    df_cat_expense.to_csv("df_cat_expense.csv")
    data_return = df_cat_expense.to_dict()

    return [txt1, style1, opt_expense, opt_expense, [], data_return]


# Add/Remove categoria receipt
@app.callback(
    [Output("category-div-add-receipt", "children"),
     Output("category-div-add-receipt", "style"),
     Output("select_receipt", "options"),
     Output('checklist-selected-style-receipt', 'options'),
     Output('checklist-selected-style-receipt', 'value'),
     Output('stored-cat-receipt', 'data')],
    [Input("add-category-receipt", "n_clicks"),
     Input("remove-category-receipt", 'n_clicks')],
    [State("input-add-receipt", "value"),
     State('checklist-selected-style-receipt', 'value'),
     State('stored-cat-receipt', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_receipt = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

    if n and not (txt == "" or txt == None):
        cat_receipt = cat_receipt + \
            [txt] if txt not in cat_receipt else cat_receipt
        txt1 = f'A categoria {txt} foi adicionada com sucesso!'
        style1 = {'color': 'green'}

    if n2:
        if check_delete == []:
            pass
        else:
            cat_receipt = [i for i in cat_receipt if i not in check_delete]

    opt_receipt = [{"label": i, "value": i} for i in cat_receipt]
    df_cat_receipt = pd.DataFrame(cat_receipt, columns=['Categoria'])
    df_cat_receipt.to_csv("df_cat_receipt.csv")
    data_return = df_cat_receipt.to_dict()

    return [txt1, style1, opt_receipt, opt_receipt, [], data_return]

# Add/Remove patfinder


@app.callback(
    [Output("category-div-add-patfinder", "children"),
     Output("category-div-add-patfinder", "style"),
     Output("select_patfinder", "options"),
     Output('checklist-selected-style-patfinder', 'options'),
     Output('checklist-selected-style-patfinder', 'value'),
     Output('stored-cat-patfinder', 'data')],
    [Input("add-category-patfinder", "n_clicks"),
     Input("remove-category-patfinder", 'n_clicks')],
    [State("input-add-patfinder", "value"),
     State('checklist-selected-style-patfinder', 'value'),
     State('stored-cat-patfinder', 'data')]
)
def add_patfinder(n, n2, txt, check_delete, data):
    cat_patfinder = list(data["Desbravador"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt == None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma novo desbravador."
            style1 = {'color': 'red'}

    if n and not (txt == "" or txt == None):
        cat_patfinder = cat_patfinder + \
            [txt] if txt not in cat_patfinder else cat_patfinder
        txt1 = f'O desbravador {txt} foi adicionado(a) com sucesso!'
        style1 = {'color': 'green'}

    if n2:
        if check_delete == []:
            pass
        else:
            cat_patfinder = [i for i in cat_patfinder if i not in check_delete]

    opt_patfinder = [{"label": i, "value": i} for i in cat_patfinder]
    df_cat_patfinder = pd.DataFrame(cat_patfinder, columns=['Desbravador'])
    df_cat_patfinder.to_csv("df_cat_patfinder.csv")
    data_return = df_cat_patfinder.to_dict()

    return [txt1, style1, opt_patfinder, opt_patfinder, [], data_return]

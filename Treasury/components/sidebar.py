import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Dbv - Tesouraria", className="text-primary"),
    html.P("By FilipeNdsa", className="text-info"),
    html.Hr(),

    # ========= Perfil ========= #
    dbc.Button(id='button_avatar',
               children=[html.Img(src='assets/img_hom.png', id='avatar_change', alt='Avatar', className='profile_avatar')
                         ], style={'background-color': 'transparent', 'border-color': 'transparent'}),

    # ========= New ========= #
    dbc.Row([
        dbc.Col([
            dbc.Button(color='success', id='open-new-receipt',
                       children=['+ Receita'])
        ], width=6),
        dbc.Col([
            dbc.Button(color='danger', id='open-new-expense',
                       children=['- Despesa'])
        ], width=6)
    ]),
    # ========= Modal Receita ========= #
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
        dbc.ModalBody([
            dbc.Col([
                dbc.Label('Descrição: '),
                dbc.Input(
                    placeholder="Ex: Campori, inscrição, brindes...", id="txt-receipt"),
            ], width=6),
            dbc.Col([
                dbc.Label('Valor: '),
                dbc.Input(
                    placeholder="Ex: R$100,00", id="value_receipt", value=""),
            ], width=6),
            dbc.Row([
                dbc.Col([
                    dbc.Label("Data: "),
                    dcc.DatePickerSingle(id='date-receipts',
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
                                 {"label": "Receita Recorrente", "value": 2}],
                        value=[1],
                        id="switches-input-receipt",
                        switch=True),
                ], width=4),
                dbc.Col([
                    html.Label("Categoria da receita"),
                    # {"label": i, "value": i} for i in cat_receipt cat_receipt[0]
                    dbc.Select(id="select_receipt", options=[], value=[])
                ], width=4),
                dbc.Col([
                    html.Label("Desbravador"),
                    # {"label": i, "value": i} for i in cat_patfinder cat_patfinder[0]
                    dbc.Select(id="select_patfinder",
                               options=[], value=[])
                ], width=4)
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
                                    options=[],  # "label": i, "value": i} for i in cat_receipt}
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
                    ], title="Adicionar/Remover Categorias",
                    ),
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
                                    type="text", placeholder="Nome Desbravador...", id="input-add-patfinder", value=""),
                                html.Br(),
                                dbc.Button(
                                    "Adicionar", className="btn btn-success", id="add-category-patfinder", style={"margin-top": "20px"}),
                                html.Br(),
                                html.Div(
                                    id="category-div-add-patfinder", style={}),
                            ], width=6),

                            dbc.Col([
                                html.Legend("Excluir desbravadores", style={
                                    'color': 'red'}),
                                dbc.Checklist(
                                    id="checklist-selected-style-patfinder",
                                    options=[],  # "label": i, "value": i} for i in cat_patfinder}
                                    value=[],
                                    label_checked_style={
                                        "color": "red"},
                                    input_checked_style={"backgroundColor": "#fa7268",
                                                         "borderColor": "#ea6258"},
                                ),
                                dbc.Button(
                                    "Remover", color="warning", id="remove-patfinder", style={"margin-top": "20px"}),
                            ], width=6)
                        ]),
                    ], title="Adicionar/Remover Desbravadores",
                    ),
                ], flush=True, start_collapsed=True, id='accordion-receipt'),

                html.Div(id="id_teste_receipt", style={"padding-top": "20px"}),

                dbc.ModalFooter([
                    dbc.Button(
                        "Adicionar Receita", id="save_receipt", color="success"),
                    dbc.Popover(dbc.PopoverBody(
                        "Receita Salva"), target="save_receipt", placement="left", trigger="click"),
                ])
            ], style={"margin-top": "25px"}),
        ])
    ], id='modal-new-expense'),

    # ========= Modal Despesa ========= #
    dbc.Modal([
        dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
        dbc.ModalBody([

        ])
    ], id='modal-new-expense'),
    # ========= Nav ========= #
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
        dbc.NavLink("Extratos", href="/extratos", active="exact"),
    ], vertical=True, pills=True, id='nav_buttons', style={'margin-bottom': '50px'}),
], id='sidebar_completed')


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-new-receipt', 'is_open'),
    Input('open-new-receipt', 'n_clicks'),
    State('modal-new-receipt')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

 # Pop-up despesa


@app.callback(
    Output('modal-new-expense', 'is_open'),
    Input('open-new-expense', 'n_clicks'),
    State('modal-new-expense')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

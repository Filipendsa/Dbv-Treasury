import pandas as pd
import os

if ("df_expense.csv" in os.listdir()) and ("df_receipts.csv" in os.listdir()):
    df_expense = pd.read_csv("df_expense.csv", index_col=0, parse_dates=True)
    df_receipts = pd.read_csv("df_receipts.csv", index_col=0, parse_dates=True)
    df_expense["Data"] = pd.to_datetime(df_expense["Data"])
    df_receipts["Data"] = pd.to_datetime(df_receipts["Data"])
    df_expense["Data"] = df_expense["Data"].apply(lambda x: x.date())
    df_receipts["Data"] = df_receipts["Data"].apply(lambda x: x.date())

else:
    data_structure = {'Valor': [],
                      'Efetuado': [],
                      'Fixo': [],
                      'Data': [],
                      'Categoria': [],
                      'Desbravador': [],
                      'Descrição': [], }

    df_receipts = pd.DataFrame(data_structure)
    df_expense = pd.DataFrame(data_structure)
    df_expense.to_csv("df_expense.csv")
    df_receipts.to_csv("df_receipts.csv")


if ("df_cat_receipt.csv" in os.listdir()) and ("df_cat_expense.csv" in os.listdir()):
    df_cat_receipt = pd.read_csv("df_cat_receipt.csv", index_col=0)
    df_cat_expense = pd.read_csv("df_cat_expense.csv", index_col=0)
    cat_receita = df_cat_receipt.values.tolist()
    cat_despesa = df_cat_expense.values.tolist()

else:
    cat_receita = {'Categoria': ["Inscrição",
                                 "Mensalidade", "Doação", "Vendas-Trufas"]}
    cat_despesa = {'Categoria': ["Trunfos",
                                 "Brindes", "Diversos", "Compra-Trufas"]}

    df_cat_receipt = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_expense = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_receipt.to_csv("df_cat_receipt.csv")
    df_cat_expense.to_csv("df_cat_expense.csv")

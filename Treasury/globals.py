import pandas as pd
import os

if ("df_expense.csv" in os.listdir()) and ("df_receipt.csv" in os.listdir()):

    df_expense = pd.read_csv("df_expense.csv", index_col=0, parse_dates=True)
    df_receipt = pd.read_csv("df_receipt.csv", index_col=0, parse_dates=True)

    df_expense["Data"] = pd.to_datetime(df_expense["Data"])
    df_receipt["Data"] = pd.to_datetime(df_receipt["Data"])

    df_expense["Data"] = df_expense["Data"].apply(lambda x: x.date())
    df_receipt["Data"] = df_receipt["Data"].apply(lambda x: x.date())

else:
    data_structure = {'Valor': [],
                      'Efetuado': [],
                      'Fixo': [],
                      'Data': [],
                      'Categoria': [],
                      'Desbravador': [],
                      'Descrição': [], }

    df_receipt = pd.DataFrame(data_structure)
    df_expense = pd.DataFrame(data_structure)

    df_expense.to_csv("df_expense.csv")
    df_receipt.to_csv("df_receipt.csv")


if ("df_cat_receipt.csv" in os.listdir()) and ("df_cat_expense.csv" in os.listdir()) and ("df_dbv_patfinder.csv" in os.listdir()):
    df_cat_receipt = pd.read_csv("df_cat_receipt.csv", index_col=0)
    df_cat_expense = pd.read_csv("df_cat_expense.csv", index_col=0)
    df_dbv_patfinder = pd.read_csv("df_dbv_patfinder.csv", index_col=0)

    cat_receipt = df_cat_receipt.values.tolist()
    cat_expense = df_cat_expense.values.tolist()
    dbv_patfinder = df_dbv_patfinder.values.tolist()

else:
    cat_receipt = {'Categoria': ["Inscrição",
                                 "Mensalidade", "Doação", "Vendas-Trufas"]}
    cat_expense = {'Categoria': ["Trunfos",
                                 "Brindes", "Diversos", "Compra-Trufas"]}
    dbv_patfinder = {'Desbravador': ["Filipe Nogueira",
                                     "Alexandra Santos", "Anna Karolinny", "Ilberty Lucas"]}

    df_cat_receipt = pd.DataFrame(cat_receipt, columns=['Categoria'])
    df_cat_expense = pd.DataFrame(cat_expense, columns=['Categoria'])
    df_dbv_patfinder = pd.DataFrame(dbv_patfinder, columns=['Desbravador'])

    df_cat_receipt.to_csv("df_cat_receipt.csv")
    df_cat_expense.to_csv("df_cat_expense.csv")
    df_dbv_patfinder.to_csv("df_dbv_patfinder.csv")

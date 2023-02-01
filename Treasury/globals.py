import pandas as pd
import os

if ("df_expenses.csv" in os.listdir()) and ("df_receipts.csv" in os.listdir()):

    df_expenses = pd.read_csv("df_expenses.csv", index_col=0, parse_dates=True)
    df_receipts = pd.read_csv("df_receipts.csv", index_col=0, parse_dates=True)

    df_expenses["Data"] = pd.to_datetime(df_expenses["Data"])
    df_receipts["Data"] = pd.to_datetime(df_receipts["Data"])

    df_expenses["Data"] = df_expenses["Data"].apply(lambda x: x.date())
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
    df_expenses = pd.DataFrame(data_structure)

    df_expenses.to_csv("df_expenses.csv")
    df_receipts.to_csv("df_receipts.csv")


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

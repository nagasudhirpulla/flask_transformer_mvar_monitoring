import pandas as pd


def getTransData():
    df = pd.read_excel('employees.xlsx')
    return df.to_dict('records')

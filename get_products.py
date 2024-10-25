import pandas as pd


def get_products(path_to_file):
    rows = []
    df = pd.read_excel(path_to_file)
    for i in range(9, len(df)):
        if df.values[i][0] == "Итого:":
            break
        rows.append(df.values[i][:-1])
    return rows


if __name__ == "__main__":

    cols = get_products("2024/Уведомление о выкупе №1000510072 от 2024-05-27.xlsx")

    for col in cols:
        print(col[1])

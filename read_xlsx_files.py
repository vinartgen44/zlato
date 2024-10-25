import pandas as pd


def read_xlsx_files(file_name: str, skippers: int = 9) -> pd.DataFrame | None:
    df = pd.read_excel(
        file_name
    )
    return df


print(read_xlsx_files("2024/Уведомление о выкупе №1000255835 от 2024-04-01.xlsx"))
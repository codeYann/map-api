from typing import List
import pandas as pd
import os

__base_dir = os.path.abspath(os.path.dirname(__file__))


def __format_columns_names(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame.columns = data_frame.columns.str.upper().str.replace(" ", "_")
    return data_frame


def read_geolocation_data(nrows: int) -> pd.DataFrame:
    file_path = os.path.join(__base_dir, "../../utils", "VAZAMENTOS_2021.xlsx")
    df = pd.read_excel(
        file_path,
        index_col=[0],
        nrows=nrows,
    )
    return __format_columns_names(df)


def select_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns]

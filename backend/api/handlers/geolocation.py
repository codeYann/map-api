# from typing import Optional
from typing import List
import pandas as pd


def __format_columns_names(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame.columns = data_frame.columns.str.upper().str.replace(" ", "_")
    return data_frame


def read_geolocation_data(nrows: int) -> pd.DataFrame:
    df = pd.read_excel(
        "/home/codeyan/projects/map-api/backend/utils/VAZAMENTOS_2021.xlsx",
        index_col=[0],
        nrows=nrows,
    )
    return __format_columns_names(df)


def select_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    return df[columns]

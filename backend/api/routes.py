from fastapi import APIRouter
from .handlers.geolocation import read_geolocation_data, select_columns

router = APIRouter()


@router.get("/geolocation")
async def read_data():
    df_wrapper = read_geolocation_data(nrows=120)
    df = select_columns(df_wrapper, ["LATITUDE", "LONGITUDE"])
    df["LATITUDE"] = df["LATITUDE"].astype(str)
    df["LONGITUDE"] = df["LONGITUDE"].astype(str)
    return df.to_dict(orient="records")

from enum import Enum
import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
import datetime as dt
from dotenv import load_dotenv
from geosyspy.geosys import Region,Env
import json
from sub_entity_analysis.sub_entity_analysis import SubEntityAnalysis


app = FastAPI(
    docs_url=None,
    title="SubEntityAnalysisApi",
    description= "Api to generate times series with GeosysPy and compare them between each other."
    )

app.mount("/static", StaticFiles(directory="./api/files"), name="static")

@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="SubEntityAnalysisApi",
        swagger_favicon_url="/static/favicon.svg"
    )

class Item(BaseModel):
    polygon: str
    subPolygon: str
    startDate: dt.date
    endDate:  dt.date

class SingleItem(BaseModel):
    polygon: str    
    startDate: dt.date
    endDate:  dt.date

class Indicator(Enum):
    """
    Available Index values 
    """
    NDVI = "NDVI"
    EVI = "EVI"
    GNDVI = "GNDVI"
    NDWI = "NDWI"
    CVI = "CVI"
    CVIn = "CVIn"
    LAI = "LAI"    

def serialize_datetime(obj):
    if isinstance(obj, dt.datetime):
        return obj.isoformat()

load_dotenv()


@app.post("/sub-entity-analysis/percentage-deviation", tags=["Analytic Computation"])
async def sub_entity_analysis_percentage_deviation(item: Item, indicator: Indicator):
    API_CLIENT_ID = os.getenv('API_CLIENT_ID')
    API_CLIENT_SECRET = os.getenv('API_CLIENT_SECRET')
    API_USERNAME = os.getenv('API_USERNAME')
    API_PASSWORD = os.getenv('API_PASSWORD')

    client = SubEntityAnalysis(API_CLIENT_ID, API_CLIENT_SECRET, API_USERNAME, API_PASSWORD, Env.PROD, Region.NA)

    start_date = dt.datetime(item.startDate.year, item.startDate.month, item.startDate.day)
    end_date = dt.datetime(item.endDate.year, item.endDate.month, item.endDate.day)

    # get the indicator index values by pixel over the defined period for the main polygon
    polygon_ds = client.get_satellite_image_time_series_indicator(item.polygon, start_date, end_date, indicator.value.lower())

    # get the indicator index values by pixel over the defined period for the sub polygon
    sub_polygon_ds = client.get_satellite_image_time_series_indicator(item.subPolygon, start_date, end_date,  indicator.value.lower())

    # compute the cumulative index value over the defined period for the main polygon
    cumulative_polygon_da = client.get_cumulative_index_calculation(polygon_ds,  indicator.value.lower())

    # compute the cumulative index value over the defined period for the sub polygon
    cumulative_sub_polygon_da = client.get_cumulative_index_calculation(sub_polygon_ds,  indicator.value.lower())

    # compute the percentage deviation between the 2 cumulative data array
    percentage_deviation = client.get_deviation_percentage(cumulative_polygon_da, cumulative_sub_polygon_da)

    # convert DataArray in dictionnary
    result = percentage_deviation.to_dict()

    # json serilization
    json_data = json.dumps(result, default=serialize_datetime, separators=(",", ":"), ensure_ascii=False)

    response = JSONResponse(content=json_data)    
    response.headers["Content-Type"] = "application/json; charset=utf-8"

    return response



@app.post("/sub-entity-analysis/cumulative-indicator-values", tags=["Analytic Computation"])
async def sub_entity_analysis_cumulative_index_values(item: SingleItem, indicator: Indicator):
    API_CLIENT_ID = os.getenv('API_CLIENT_ID')
    API_CLIENT_SECRET = os.getenv('API_CLIENT_SECRET')
    API_USERNAME = os.getenv('API_USERNAME')
    API_PASSWORD = os.getenv('API_PASSWORD')

    client = SubEntityAnalysis(API_CLIENT_ID, API_CLIENT_SECRET, API_USERNAME, API_PASSWORD, Env.PROD, Region.NA)

    start_date = dt.datetime(item.startDate.year, item.startDate.month, item.startDate.day)
    end_date = dt.datetime(item.endDate.year, item.endDate.month, item.endDate.day)

    # get the indicator index values by pixel over the defined period for the main polygon
    polygon_ds = client.get_satellite_image_time_series_indicator(item.polygon, start_date, end_date,  indicator.value.lower())
    
    # compute the cumulative index value over the defined period for the main polygon
    cumulative_polygon_da = client.get_cumulative_index_calculation(polygon_ds,  indicator.value.lower())    

    # convert DataArray in dictionnary
    result = cumulative_polygon_da.to_dict()

    # json serilization
    json_data = json.dumps(result, default=serialize_datetime,separators=(",", ":"), ensure_ascii=False)
    
    response = JSONResponse(content=json_data)    
    response.headers["Content-Type"] = "application/json; charset=utf-8"

    return response

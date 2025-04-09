from fastapi import FastAPI, Query,HTTPException
from geoip2.database import Reader
import os

app = FastAPI()

GEOIP_DB_PATH = r"C:\Users\pc\Downloads\GeoLite2-City_20250408\GeoLite2-City_20250408\GeoLite2-City.mmdb"

@app.get("/ip-to-country/")
def get_country(ip: str = Query(..., description="IP address to lookup")):
    try:
        with Reader(GEOIP_DB_PATH) as reader:
            response = reader.city(ip)
            return {
                "ip": ip,
                "country": response.country.name,
                "city": response.city.name,
                "continent": response.continent.name
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
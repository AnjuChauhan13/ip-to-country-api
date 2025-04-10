# from fastapi import FastAPI, Query,HTTPException
# from geoip2.database import Reader
# import os

# app = FastAPI()

# GEOIP_DB_PATH = r"C:\Users\pc\Downloads\GeoLite2-City_20250408\GeoLite2-City_20250408\GeoLite2-City.mmdb"

# @app.get("/ip-to-country/")
# def get_country(ip: str = Query(..., description="IP address to lookup")):
#     try:
#         with Reader(GEOIP_DB_PATH) as reader:
#             response = reader.city(ip)
#             return {
#                 "ip": ip,
#                 "country": response.country.name,
#                 "city": response.city.name,
#                 "continent": response.continent.name
#             }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
import os
import requests

def download_db():
    db_folder = "geo"
    db_path = os.path.join(db_folder, "GeoLite2-City.mmdb")
    if not os.path.exists(db_path):
        os.makedirs(db_folder, exist_ok=True)
        print("Downloading GeoLite2-City.mmdb...")
        url = "https://drive.google.com/file/d/1CtZYRoVwVbJACDSiik5bVL2IbA0OjHvc/view?usp=drive_link"  # Replace with your own
        response = requests.get(url)
        with open(db_path, "wb") as f:
            f.write(response.content)
    return db_path

GEOIP_DB_PATH = download_db()

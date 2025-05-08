# Extracción de días festivos con FastAPI

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Inicializar la app

app = FastAPI()

# URL del sitio 

URL = {"URL": "https://www.festivos.com.co/historico"}

# Diccionario de meses

months = {

    "enero": "01", "febrero": "02", "marzo": "03",
    "abril": "04", "mayo": "05", "junio": "06",
    "julio": "07", "agosto": "08", "septiembre": "09",
    "octubre": "10", "noviembre": "11", "diciembre": "12"
}


class Scrapper:

    @staticmethod

    def extract_data(URL):

        fechas = []

        response = requests.get(URL["URL"])
        soup = BeautifulSoup(response.text, "html.parser")

        for row in soup.find("tbody").find_all("tr"):

            rows = row.findAll("td")
            year = rows[0].text
            text = str(rows[1].text)
            clean_text = text.split(" de ")
            date = f"{clean_text[0]}/{months[clean_text[1]]}/{year}"
            fechas.append(date)

        return fechas

# Ruta de la API:

@app.get("/festivos")

def get_festivos():

    try:

        scrapper = Scrapper()
        fechas = scrapper.extract_data(URL)
        df = pd.DataFrame(fechas, columns=["fecha"])

        return JSONResponse(content=df.to_dict(orient="records"))
    
    except Exception as e:
        
        return JSONResponse(content={"error": str(e)}, status_code=500)

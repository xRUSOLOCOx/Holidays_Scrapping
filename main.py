## Extraccion de dias festivos Scrapping ##

# Importar librerias necesarias:

from flask import Flask, jsonify

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Datos del sitio web a extraer:

URL = {"URL": "https://www.festivos.com.co/historico"}

# Diccionario de meses:

months = {
    "enero": "01", "febrero": "02", "marzo": "03",
    "abril": "04", "mayo": "05", "junio": "06",
    "julio": "07", "agosto": "08", "septiembre": "09",
    "octubre": "10", "noviembre": "11", "diciembre": "12"
}

# Clase Scrapper
class Scrapper:

    @staticmethod
    def extract_data(URL):

        fechas = []

        request = requests.get(URL["URL"])
        soup = BeautifulSoup(request.text, "html.parser")

        for row in soup.find("tbody").find_all("tr"):

            rows = row.findAll("td")
            year = rows[0].text
            text = str(rows[1].text)
            clean_text = text.split(" de ")

            date = f"{clean_text[0]}/{months[clean_text[1]]}/{year}"
            fechas.append(date)

        return fechas

# Inicializar Flask

app = Flask(__name__)

# Ruta API
@app.route("/festivos", methods=["GET"])

def get_festivos():

    try:

        scrapper = Scrapper()
        fechas = scrapper.extract_data(URL)

        df = pd.DataFrame(fechas, columns=["fecha"])

        return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Para entorno local

if __name__ == "__main__":
    app.run(debug=True)



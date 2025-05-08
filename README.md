# API de Días Festivos en Colombia

Este proyecto consiste en una API desarrollada en Python utilizando Flask, que realiza web scraping sobre el sitio [festivos.com.co](https://www.festivos.com.co/historico). El objetivo es extraer y exponer de manera estructurada las fechas históricas de días festivos en Colombia a través de una interfaz JSON que puede ser utilizada en una interfaz SQL o PowerQuery ETC.

---

## ⚙️ Descripción General

La aplicación consulta una tabla HTML alojada en el sitio mencionado anteriormente, extrae la información correspondiente a las fechas de los festivos desde el año 1984 hasta la actualidad, y la transforma en un formato accesible mediante una petición HTTP tipo `GET`. (El script se actualiza a medida de que el sitio fuente cargue mas datos.
---

## Tecnologías y dependencias utilizadas

- Python 3.12  
- Flask  
- Requests  
- BeautifulSoup4  
- Pandas  


---

## Instalación

Para ejecutar el proyecto de manera local, siga los siguientes pasos:

1. Clonar el repositorio:

https://github.com/xRUSOLOCOx/Holidays_Scrapping.git

instalar dependencias en consola directamente desde requirements:

pip install -r requirements.txt

ejecución:

python main.py

---

## Salidas tipo JSON:

[
  {
    "fecha": "1/01/2020"
  },
  {
    "fecha": "6/01/2020"
  },
  ...
]



## Despliegue

Codigo Totalmente preparado para despliegue en Railway




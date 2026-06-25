# Demo para ejecutar en Jupyter o cualquier editor Python
#
# Este script usa la misma lógica que el bloque original:
# - lee un archivo Excel con columna entityId
# - crea la URL de Dynatrace con dominio ejemplo
# - usa token "abc"
# - ejecuta un POST por cada host

import requests
import json
import pandas as pd

# Cambia el nombre del archivo si es necesario
excel_path = "demo_hostids.xlsx"

df = pd.read_excel(excel_path)
lista = df["entityId"].tolist()
i = 0
for j in lista:
    HostID = str(lista[i])
    api_token = "abc"
    URL = "https://ejemplo.live.dynatrace.com/api/v2/settings/objects?validateOnly=false"

    header = {
        'accept': 'application/json; charset=utf-8',
        'Authorization': 'Api-Token ' + str(api_token),
        'Content-Type': 'application/json; charset=utf-8'
    }

    dataOA = '[{"schemaId":"builtin:host.monitoring","schemaVersion":"1.3","scope":"' + HostID + '","value":{"enabled":false,"autoInjection":true}}]'

    params = {
        "format": "json"
    }

    response = requests.post(url=URL, headers=header, data=dataOA)
    print(response.text)
    i += 1

# Dynatrace API Toolkit

Toolkit de ejemplo para interactuar con Dynatrace API usando Python.

## Estructura

- `dynatrace_api_toolkit/`: paquete Python
- `dynatrace_api_toolkit/config.py`: configuración base y variables de entorno
- `dynatrace_api_toolkit/client.py`: funciones de API
- `dynatrace_api_toolkit/utils.py`: utilidades de tiempo y lectura de Excel
- `requirements.txt`: dependencias

## Configuración

Define los valores en variables de entorno o pásalos a los scripts:

```bash
export DT_API_TOKEN="tu_token"
export DT_BASE_URL="https://ejemplo.live.dynatrace.com"
```

## Instalación

```bash
python -m pip install -r requirements.txt
```

## Uso

Deshabilitar la monitorización de un host group desde un Excel:

```bash
python run_disable_oa.py --excel /ruta/archivo.xlsx --token "$DT_API_TOKEN"
```

Obtener datos de OneAgents para un host group:

```bash
python run_get_oneagents.py --hostgroup HOST_GROUP-... --from "05.09.2025 00:00" --to "05.09.2025 10:00" --output /ruta/salida.xlsx --token "$DT_API_TOKEN"
```

## Notebook demo

Hay un notebook de ejemplo diseñado para ejecutar el mismo flujo tipo Jupyter con URL de ejemplo y token fijo `abc`.

- Archivo: `DisabledOA_demo.ipynb`
- Usa una hoja de Excel con columna `entityId`
- La URL fija es `https://ejemplo.live.dynatrace.com`
- El token fijo es `abc`

Para usarlo:

1. Abre `DisabledOA_demo.ipynb` en Jupyter.
2. Asegúrate de tener un archivo Excel válido, por ejemplo `demo_hostids.xlsx`.
3. Corre la celda Python que lee el Excel y hace el POST por cada `HostID`.

## Ejecución paso a paso

1. Instala las dependencias:

```bash
python3 -m pip install -r requirements.txt
```

2. Exporta el token y la URL base de Dynatrace:

```bash
export DT_API_TOKEN="tu_token"
export DT_BASE_URL="https://ejemplo.live.dynatrace.com"
```

3. Ejecuta el script de deshabilitar monitorización:

```bash
python3 run_disable_oa.py --excel /ruta/archivo.xlsx --token "$DT_API_TOKEN"
```

4. Ejecuta el script de obtención de OneAgents:

```bash
python3 run_get_oneagents.py --hostgroup HOST_GROUP-... --from "05.09.2025 00:00" --to "05.09.2025 10:00" --output /ruta/salida.xlsx --token "$DT_API_TOKEN"
```

## Notas

- El dominio Dynatrace se fija en `https://ejemplo.live.dynatrace.com`
- No dejes tokens en texto plano en los archivos de código

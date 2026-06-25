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

## Ejecución paso a paso

1. Asegúrate de estar en el directorio del proyecto:

```bash
cd /Users/jenifersanchez/Documents/DynatraceScripts/DynaApiTools
```

2. Instala las dependencias:

```bash
python3 -m pip install -r requirements.txt
```

3. Exporta el token y, si quieres, la URL base:

```bash
export DT_API_TOKEN="tu_token"
export DT_BASE_URL="https://ejemplo.live.dynatrace.com"
```

4. Ejecuta el script de deshabilitar monitorización:

```bash
python3 run_disable_oa.py --excel /ruta/archivo.xlsx --token "$DT_API_TOKEN"
```

5. Ejecuta el script de obtención de OneAgents:

```bash
python3 run_get_oneagents.py --hostgroup HOST_GROUP-... --from "05.09.2025 00:00" --to "05.09.2025 10:00" --output /ruta/salida.xlsx --token "$DT_API_TOKEN"
```

## Push a GitHub

1. Comprueba el estado y la rama:

```bash
git status
```

2. Agrega los cambios:

```bash
git add .
```

3. Haz commit con un mensaje descriptivo:

```bash
git commit -m "Actualizar toolkit Dynatrace y ejemplo de ejecución"
```

4. Envía al repositorio remoto:

```bash
git push origin main
```

## Notas

- El dominio Dynatrace se fija en `https://ejemplo.live.dynatrace.com`
- No dejes tokens en texto plano en los archivos de código

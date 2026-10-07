"""
Demostracion del patron Factory Method. Corra: python demo.py

El mismo generar(datos) produce un reporte CSV o JSON segun el
generador que se elija; generar no sabe cual Exportador recibe.
"""

from reportes import GeneradorCSV, GeneradorJSON

ventas = [
    {"producto": "Cafe", "cantidad": 3},
    {"producto": "Te", "cantidad": 5},
]

if __name__ == "__main__":
    for generador in (GeneradorCSV(), GeneradorJSON()):
        print(f"--- {type(generador).__name__} ---")
        print(generador.generar(ventas))

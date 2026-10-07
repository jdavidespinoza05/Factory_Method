"""
Dos pruebas del patron Factory Method. Ambas fallan si generar()
deja de pedir el exportador al metodo fabrica (por ejemplo, si
alguien mete un if por formato dentro de GeneradorReporte).
"""

from reportes import Exportador, GeneradorReporte

DATOS = [{"producto": "Cafe", "cantidad": 3}]


def test_un_formato_nuevo_funciona_sin_tocar_generador_reporte():
    class ExportadorTextoPlano(Exportador):
        def exportar(self, datos):
            return "; ".join(f"{r['producto']}={r['cantidad']}" for r in datos)

    class GeneradorTextoPlano(GeneradorReporte):
        def crear_exportador(self):
            return ExportadorTextoPlano()

    assert GeneradorTextoPlano().generar(DATOS) == "Cafe=3"


def test_generar_usa_exactamente_el_producto_del_metodo_fabrica():
    class ExportadorEspia(Exportador):
        def __init__(self):
            self.recibido = []

        def exportar(self, datos):
            self.recibido.append(datos)
            return "respuesta del espia"

    espia = ExportadorEspia()

    class GeneradorConEspia(GeneradorReporte):
        def crear_exportador(self):
            return espia

    resultado = GeneradorConEspia().generar(DATOS)

    assert espia.recibido == [DATOS]
    assert resultado == "respuesta del espia"

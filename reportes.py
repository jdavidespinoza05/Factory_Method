"""
Patron Factory Method aplicado a la exportacion de reportes.

Roles del patron (con sus nombres en este ejemplo):
- Producto          -> Exportador
- ProductoConcreto  -> ExportadorCSV, ExportadorJSON
- Creador           -> GeneradorReporte
- CreadorConcreto   -> GeneradorCSV, GeneradorJSON
"""

import json
from abc import ABC, abstractmethod


class Exportador(ABC):
    """Producto: convierte una lista de registros en texto."""

    @abstractmethod
    def exportar(self, datos: list[dict]) -> str:
        raise NotImplementedError


class ExportadorCSV(Exportador):
    """ProductoConcreto: una linea de encabezados y una linea por registro."""

    def exportar(self, datos: list[dict]) -> str:
        columnas = list(datos[0].keys())
        lineas = [",".join(columnas)]
        for registro in datos:
            lineas.append(",".join(str(registro[c]) for c in columnas))
        return "\n".join(lineas)


class ExportadorJSON(Exportador):
    """ProductoConcreto: los registros como un arreglo JSON."""

    def exportar(self, datos: list[dict]) -> str:
        return json.dumps(datos, ensure_ascii=False, indent=2)


class GeneradorReporte(ABC):
    """
    Creador: tiene el proceso comun (generar) y declara el metodo
    fabrica (crear_exportador). generar nunca nombra una clase concreta.
    """

    @abstractmethod
    def crear_exportador(self) -> Exportador:
        """Metodo fabrica: cada subclase decide que Exportador crear."""
        raise NotImplementedError

    def generar(self, datos: list[dict]) -> str:
        if not datos:
            raise ValueError("El reporte necesita al menos un registro")
        exportador = self.crear_exportador()
        return exportador.exportar(datos)


class GeneradorCSV(GeneradorReporte):
    """CreadorConcreto: produce un ExportadorCSV."""

    def crear_exportador(self) -> Exportador:
        return ExportadorCSV()


class GeneradorJSON(GeneradorReporte):
    """CreadorConcreto: produce un ExportadorJSON."""

    def crear_exportador(self) -> Exportador:
        return ExportadorJSON()

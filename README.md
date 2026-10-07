# Factory Method - Exportación de reportes

Implementación mínima del patrón **Factory Method** para la tarea de
Patrones de Diseño.

Autores:
- Jose David Espinoza Brenes - carné 2023145994
- Jeremmy Aguilar Villanueva - carné 2022191791

## Qué hace

`GeneradorReporte` tiene un proceso común, `generar(datos)`, que
necesita un `Exportador` para convertir los registros en texto. En vez
de construirlo con `ExportadorCSV()` o `ExportadorJSON()` directamente,
lo pide al **método fábrica** `crear_exportador()`, que cada subclase
(`GeneradorCSV`, `GeneradorJSON`) redefine.

| Rol del patrón     | Clase en este ejemplo               |
|--------------------|-------------------------------------|
| Producto           | `Exportador`                        |
| Producto concreto  | `ExportadorCSV`, `ExportadorJSON`   |
| Creador            | `GeneradorReporte`                  |
| Creador concreto   | `GeneradorCSV`, `GeneradorJSON`     |

Para agregar un formato nuevo basta con crear un exportador y su
generador; `GeneradorReporte.generar` no se modifica.

## Cómo correrlo

Requiere Python 3.9 o superior. Desde una terminal en esta carpeta:

```bash
python -m pip install pytest

# Demostración: el mismo reporte en CSV y en JSON
python demo.py

# Pruebas
python -m pytest -v
```

En macOS o Linux puede ser `python3` en lugar de `python`.

## Qué demuestra cada prueba

**`test_un_formato_nuevo_funciona_sin_tocar_generador_reporte`**
Define dentro de la prueba un formato que `GeneradorReporte` nunca vio
(`ExportadorTextoPlano` con su `GeneradorTextoPlano`) y comprueba que
`generar()` lo usa sin cambiar ni una línea de `GeneradorReporte`. Si
alguien eligiera el formato con un `if` dentro de `generar()`, el
formato nuevo no estaría contemplado y la prueba fallaría.

**`test_generar_usa_exactamente_el_producto_del_metodo_fabrica`**
Usa un `ExportadorEspia`, un producto falso que anota qué datos
recibió. Comprueba que `generar()` trabaja con el mismo objeto que
devuelve `crear_exportador()`: le pasa los datos sin cambiarlos y
devuelve exactamente lo que el exportador respondió. Si `generar()`
construyera su propio exportador en vez de pedirlo al método fábrica,
el espía no recibiría nada y la prueba fallaría.

La primera prueba cubre la **extensión** sin modificar el Creador; la
segunda, que el Creador realmente **delega** la creación.

## Archivos

```
reportes.py        Producto, productos concretos, Creador y creadores concretos
demo.py            ejemplo de uso (python demo.py)
test_reportes.py   las dos pruebas (pytest)
README.md          este archivo
```

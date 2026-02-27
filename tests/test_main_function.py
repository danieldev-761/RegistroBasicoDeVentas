"""Prueba básica (smoke test) para la función principal.

El script de prueba original intentaba importar ``src.app`` de forma directa,
lo cual falla cuando el archivo se ejecuta como un script porque ``python``
únicamente añade al ``sys.path`` el directorio que contiene el script
(``tests/``).  En esa situación el paquete ``src`` no es visible y se
produce un ``ModuleNotFoundError``.

Para poder importar la función tanto al ejecutar el módulo como al ejecutar el
archivo directamente, ajustamos ``sys.path`` para incluir la raíz del proyecto.
Esto imita el comportamiento de un ejecutor de pruebas como ``pytest`` que lo
hace automáticamente.
"""

import os
import sys

#para asegurar de que la raíz del proyecto esté en «sys.path» para que se pueda importar «src».
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import registroVentas


def test_registroVentas_import():
    """Verifica que la función puede importarse y es invocable."""
    assert callable(registroVentas)


if __name__ == "__main__":
    #cuando se ejecuta el script manualmente seguimos llamando a la función
    #para que la demostración interactiva se comporte igual que antes
    registroVentas()
# RegistroBasicoDeVentas
Este es un proyecto para registrar una venta, aplicando las reglas del negocio. Finalmente, mostrar en consola información pertinente sobre la compra.

## Registro de errores de pruebas

Durante el desarrollo se encontraron varios problemas al ejecutar los tests
manualmente. A continuación se documentan los más relevantes y las correcciones
aplicadas:

* **ImportError al ejecutar `tests/test_main_function.py` directamente**
	- Al invocar el archivo con `python tests/test_main_function.py` se obtenía
		`ModuleNotFoundError: No module named 'src'` porque el intérprete sólo
		añadía `tests/` a `sys.path`.  Se resolvió añadiendo explícitamente la
		raíz del proyecto a `sys.path` en la cabecera del test (mismo comportamiento
		que tendrían runners como `pytest`).

* **TypeError en `generar_resumen_de_venta`**
	- La función intentaba usar `clientes["membresia_vip"]` tras imprimir el
		resumen, pero `clientes` es una lista y por tanto la operación fallaba con
		`TypeError: list indices must be integers or slices, not str`.
	- La causa fue una suposición errónea sobre el alcance de la variable y la
		ausencia de argumentos que llevasen el estado del cliente. La corrección
		consiste en deducir si el comprador es VIP a partir de los diccionarios de
		`subordenes`; además se añadió un comentario explicativo.

Estas notas sirven para facilitar la comprensión de fallos de test y
garantizar que cualquier colaborador pueda recuperarlos en el futuro.


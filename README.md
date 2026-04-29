# Win11 Classic

Herramienta en Python diseñada para restaurar el menú de clic derecho clásico de Windows 10 en Windows 11 mediante la modificación del registro.

## Funciones principales
* Recuperación de menús y comportamientos clásicos de Windows.
* Modificación automática de claves de registro (Regedit).
* Interfaz directa para evitar procesos manuales complejos.

## Requisitos
* Python 3.x.
* Permisos de administrador (necesarios para modificar el registro).

## Uso
Ejecutar el script:
python "Win11 Classic.py"

Crear ejecutable (.exe):
pyinstaller --noconsole --onefile "Win11 Classic.py"

## Archivos
* Win11 Classic.py: Código fuente.
* icono.ico: Recurso visual para el ejecutable.
* .gitignore: Filtro de archivos para Git.

## Advertencia
El uso de este software es bajo responsabilidad del usuario ya que modifica configuraciones críticas del sistema.

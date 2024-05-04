from pathlib import Path

"""
Este modulo ofrece clases que representa rutas del sistema de archivos con semantica apropiada para diferentes sistemas operativos
"""

base = Path.home()
print(base)

ruta = Path(base, "Documents/code/NOTES/LANGUAJE/PYTHON")
print(ruta)


#######################################################
"""
Iterando sobre todos los archivos .txt en el arbol de directorios
"""
print("\n" + "*" * 50)
print("Iteracion de archivos .txt")
for archivo in ruta.glob("**/*.txt"):
    print(archivo)
print("\n" + "*" * 50)


#######################################################
"""
Iterando en los subdirectorios
"""
print("\n" + "*" * 50)
print("Iteracion de directorios")
for directorio in ruta.iterdir():
    if directorio.is_dir():
        print(directorio)
print("\n" + "*" * 50)


######################################################
"""
Navegacion en los arboles de directorios
"""
print("\n" + "*" * 50)
curso_udemy = ruta / "udemy"
print(curso_udemy)
print("\n" + "*" * 50)


######################################################
"""
Leer el archivo
"""
ruta_actual = Path.cwd()
print(ruta_actual)

documento = ruta_actual / "text.txt"
documento_abierto = documento.read_text()
documento_abierto_2 = documento.open("r").read()
print(documento_abierto)
print(documento_abierto_2)


######################################################
"""
Sobre escribir archivos
"""
documento_abierto_3 = documento.open("w").write("Hola soy yo de nuevo")
print(documento_abierto_3)


######################################################
"""
Escribir continuamente
"""
documento_abierto_4 = documento.open("a").write("Hola")
print(documento_abierto_4)

######################################################
"""
Cambiar nombre del directorio
"""

from pathlib import Path

"""
Este modulo ofrece clases que representa rutas del sistema de archivos con semantica apropiada para diferentes sistemas operativos
"""

base = Path.home()
print(base)

# siempre que se trabaja con una ruta se usa la clase del modulo  ( Path )
ruta = Path(base, "Documents/code/NOTES/LANGUAJE/PythonNotes/libs")
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
# curso_udemy = ruta / "udemy"  # concatenar elementos en la ruta
# joinpath() -> funciona incluso si ruta es None, Nota!!!!!!!! : buenas practicasa
directorio_librerias = ruta.joinpath("pathlib")
print("Concatenando rutas : ", directorio_librerias)
print("\n" + "*" * 50)


######################################################
"""
Leer el archivo
"""
print("\n" + "*" * 50)
ruta_actual = Path.cwd()
print(ruta_actual)

documento = ruta_actual / "text.txt"
documento_abierto = documento.read_text()
documento_abierto_2 = documento.open("r").read()
print(documento_abierto)
print(documento_abierto_2)
print("\n" + "*" * 50)


######################################################
"""
Sobre escribir archivos
"""
print("\n" + "*" * 50)
documento_abierto_3 = documento.open("w").write("Hola soy yo de nuevo")
print(documento_abierto_3)
print("\n" + "*" * 50)


######################################################
"""
Escribir en el doocumento sin sobre escribir lo que ya tenia
"""
print("\n" + "*" * 50)
documento_abierto_4 = documento.open("a").write("Hola")
print(documento_abierto_4)
print("\n" + "*" * 50)

######################################################
"""
Cambiar nombre del archivo
"""
print("\n" + "*" * 50)
print("Ruta: ", ruta)
# capturamos la ruta especifica del archivo, con el nombre del archivo que sera modificado
archivo_txt = ruta.joinpath("pathlib", "text.txt")
# creamos la nueva ruta con el nombre del archivo modificado
nueva_ruta = ruta.joinpath("pathlib", "texto.txt")
# renombramos la ruta del archivo especifico con el nuevo valor
archivo_txt.rename(nueva_ruta)
print(archivo_txt)
print("\n" + "*" * 50)

######################################################
"""
Eliminar directorio
"""

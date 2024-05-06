# Documentacion de las librerias y comandos CLI de instalacion

## LIBRERIAS :

Las librerias estan instaladas en un entorno virtual, para acceder al entorno virtual en la terminal accedemos al script activate de la carpeta env

Crear entorno virtual :

```
>>> pip install virtualenv
>>> virtualenv [nombre del entoro] : env por convencion
```

Acceder al entorno virtual

```
>>> .\env\Scripts\activate
```

Luego de ingresar instalamos las librerias que hay en el entorno global ejecutando el comando

```
>>> pip install -r .\requirements.txt
```

### Instalacion manual de cada libreria

- selenium

```
>>> pip install selenium
```

- dotenv

```
>>> pip install python-dotenv
```

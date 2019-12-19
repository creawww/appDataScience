# DOCKER PYTHON FOR FLASK

Un entorno docker para trabajar con Flask y Python

contenedor preparado para trabajar con Python: 3.7

Si necesitar otra version simplemente cambia la primera linea del dockerfile

FROM python:3.7-stretch

## construir la imagen si no existe

La primera vez que clonamos el repo necesitamos construir la imagen con nombre propio.

Si construimos la imagen con nombre se quedara en nuestro sistema y podremos usarla para todos los proyectos que la necesitemos

    docker build --no-cache --pull . -t mypython

## arrancar el contenedor

    docker run -it --rm --name=mypyapp -p 5000:5000 -v $PWD:/home/app mypython /bin/bash

Para no tener que escribir un comando tan largo he creado un **runDocker.sh**

    ./runDocker.sh

Cuando ejecutamos el script o el comando se nos abre un terminal y estamos dentro del contenedor en el que tenemos Python

# Ejecutamos pythom dentro del contenedor

    python app/app.py

para acceder a la pagina como expone el puerto 5000

http://localhost:5000/

# Proyecto_estetica

ENV-Entorno virtual

Al trabajar con github, hay ciertas carpetas que contienen muchicimos archivos. Al momento de clonar o subir estos repositorios, toman una gran cantidad de tiempo para realizarlos, es por eso que se debe de ignorarlos, ya que se pueden descargar rapidamente por separado.

Creacion de entorno: py -m venv [Entorno] 
// Recomiendo que lo llamen "venv" y que la carpeta se ubique junto al archivo manage.py

Lista de librerias:
    - Django

---------------------------------------------------------------------------------------------------------
GIT COMANDOS
---------------------------------------------------------------------------------------------------------
Tu Identidad

Lo primero que deberás hacer cuando instales Git es establecer tu nombre de usuario y dirección de correo electrónico. Esto es importante porque los "commits" de Git usan esta información, y es introducida de manera inmutable en los commits que envías:

$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com

De nuevo, sólo necesitas hacer esto una vez si especificas la opción --global, ya que Git siempre usará esta información para todo lo que hagas en ese sistema. Si quieres sobrescribir esta información con otro nombre o dirección de correo para proyectos específicos, puedes ejecutar el comando sin la opción --global cuando estés en ese proyecto.

Muchas de las herramientas de interfaz gráfica te ayudarán a hacer esto la primera vez que las uses.

---------------------------------------------------------------------------------------------------------
Clonando un repositorio existente

Puedes clonar un repositorio con git clone [url].

$ git clone https://github.com/J-Joel/Proyecto_estetica

---------------------------------------------------------------------------------------------------------
Revisando el Estado de tus Archivos

La herramienta principal para determinar qué archivos están en qué estado es el comando git status.

$ git status

Un archivo puede estar en el estado Rojo: El archivo es reconocido por git pero no esta habilitado para subirlo, Verde: El archivo ya fue habilitado y esta preparado para comfirmar el cambio al repositorio.

---------------------------------------------------------------------------------------------------------
Añadir Archivos Nuevos al repositorio

Para prepararlo o hablitar los archivos, se ejecuta el comando: $ git add
Este comando cumple varios propósitos - lo usas para empezar a añadir archivos nuevos, preparar archivos, y hacer otras cosas como marcar archivos en conflicto por combinación como resueltos

Este comando puede ir añadiendo archivos por archivos, o completamente todo el listados que se muestra con el comando $ git status.

$ git add [nombre archivo/carpeta]
$ git add . (añade todo los archivos)

---------------------------------------------------------------------------------------------------------
Confirmar Cambios

Para comfirar los cambios de los archivos añadidos por add, se debe usar el comando

$ git commit -m "Descripcion general de lo que se cambio"

Con el parametro -m indicamos el mensaje que se mostrara al realizar el cambio dentro del repositorio, este se visualizara para todos los integrantes dentro del repositorio(Es necesario tener configurado el usuario)

---------------------------------------------------------------------------------------------------------
Realizar cambios

Usa git push para insertar confirmaciones realizadas en la rama local en un repositorio remoto.

$ git push origin main
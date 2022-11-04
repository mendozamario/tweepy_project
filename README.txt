Este es un proyecto ralizado con Python3, implementando algunas librerias como tweepy y configparser
con la finalidad de mostrar un dashboard con datos y diagramas que permitan el entendimiento de este
en este momento el proyecto se encuentra en elaboración, por lo tanto solo existe una conexión con la
API de twitter y la visualización de los tweets que hay en el timeline.

Los requisitos para poder ejecutarlos primero es tener instalado python y ademas descargar las siguientes librerias
- Tweepy (pip install tweepy)
- Configparser (pip install configparser)

Para descargar el programa se puede hacer como .zip desde github.com/mendozamario/tweepy_project.git o en su defecto
si se tiene instalado git en el dispositivo donde se desee almacenar, abrir una terminal y ejecutar el codigo
git clone https://github.com/mendozamario/tweepy_project.git 

La función del programa comienza teniendo en cuenta que se necesita un nombre de usuario, tal cual como aparece en el
link del perfil de la persona que desees buscar, luego de eso se va al archivo twitter.py y en la ultima linea se coloca
el nombre de usuario sin el @.

Para ejecutarlo en la dirección de la carpeta, se abre una terminal y se ejecuta el comando:
- Linux: python3 twitter.py
- Windows: python twitter.py

Luego de eso se abre el archivo de power bi, ya sea online o en la aplicación de power bi que puede ser descargada en la
microsoft store, y ahí se va al lado izquierdo a la tercera pestaña, donde estan cargadas las tablas y sobre la tabla le da a los 3 puntos
en la parte superior derecha de esta, y va hasta la opción actualizar tabla. Luego de eso ya puede ver los graficos actualizados.


-- El programa se encuentra en desarrollo --
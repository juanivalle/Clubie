# CLUBIE
<img src="back-End/static/media/Clubie_hz_col_neg.png">

### Contenido
>  Indice de contenido.

- [Equipo de trabajo](#Equipo-de-trabajo)
- [Descripcion](#Descripcion)
- [Video demo del proyecto](#video-demo-del-proyecto)
- [Estructura del proyecto](#Estructura-del-proyecto)
- [Características](#Características)
- [Funcionalidades](#Funcionalidades)
- [Dependencias](#Dependencias)
- [Funcionalidades](#Funcionalidades)

## Equipo de trabajo
- Carlos Barrio  [@charlybarrio](https://github.com/charlybarrio) - Front-end
- Juan Ignacio Valle  [@juanivalle](https://github.com/juanivalle) - Front-end
- Neo Dau  [@NeoDau](https://github.com/NeoDau) - Front-end
- Matias Mancini [@EMME-ESSE](https://github.com/EMME-ESSE) - Back-end
- Agustin Meriles  [@AgustinMeriles](https://github.com/AgustinMeriles) - Back-end

## Descripcion
Proyecto final de [Holberton School](https://www.holbertonschool.com/) para el programa de "Full Stack Web Development".

Clubie es un sitio web diseñado para gestionar de manera eficiente el registro de clubes cannábicos. Es un proyecto enfocado en las necesidades específicas de los clubes de cannabis, con el objetivo de optimizar su trazabilidad interna, facilitar la gestión de datos y hacer visibles los registros de sus productos en la web. Todos los datos se tratan como confidenciales y se almacenan de forma segura. Solo el propietario y su equipo tienen acceso a los datos.

## Video demo del proyecto
[Video](https://youtube.com/)

## Estructura del proyecto

* adminWeb<br>
  Contiene html y funciones para poder registrar nuevos usuarios en la plataforma
  
* back-End<br>
  - instance : Contiene la base de datos
  - static : Contiene los archivos css, js e imagenes utilizadas
  - template : Contiene todos los html, diferenciados en si el usuario se encuentra logueado o no.
  - adm.py : Funciones necesarias para creacion de usuarios  
  - app.py : Funciones necesarias de clubie.
  - appadmin.py : Querys
  - clases.py : Diferentes clases que utilizamos, clubes, miembros, plantes, etc.
  - rutas.py : Rutas.
    
* node_modules<br>
  Ni idea
  
* Paquetes Json.

## Características
- Acceso único para cada club. Los creadores de CLUBIE son responsables de autorizar los clubes.
- Los clubes cargan manualmente sus datos para que queden registrados.
- Almacenamiento de todos los datos del club, ventas, plantas, con el objetivo de mantener un registro completo.

## Funcionalidades
El sitio web incluye las siguientes funcionalidades:

- Registro de usuarios: Los usuarios pueden registrarse proporcionando su cédula, nombre, teléfono y correo electrónico.
- Edición de usuarios: Los usuarios pueden editar su información personal.
- Gestión de clubes: Los usuarios pueden crear y gestionar clubes cannábicos, incluyendo la carga de archivos relacionados.
- Trazabilidad de plantas: Los usuarios pueden registrar y hacer un seguimiento de la trazabilidad de las plantas, incluyendo detalles como variedades, etapas de crecimiento, floración, cosecha, etc.
- Ventas: Los usuarios pueden registrar las ventas de productos cannábicos, incluyendo detalles como la cantidad y la fecha de retiro.

## Flowchart
<img src="flow no log">
<img src="flow log">

## Dependencias
Asegúrate de tener los siguientes requisitos instalados en tu entorno de desarrollo:
````
- Flask                2.2.3
- Flask-Bcrypt         1.0.1
- Flask-Cors           4.0.0
- Flask-Login          0.6.2
- Flask-Migrate        4.0.4
- Flask-SQLAlchemy     3.0.3
- Flask-WTF            1.1.1
- Jinja2               3.1.2
- SQLAlchemy           2.0.9
- sqlparse             0.4.4
- WTForms              3.0.1
- bcrypt               4.0.1
````
[Back to the top](#clubie)
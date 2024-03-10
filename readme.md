
<h2 align="center">Sistema de reservas de un restaurant</h2>


<h3 align="center">Proyecto en Django</h3>


<p align="center">
    Sistema de reservas de mesas para un restaurant, en el cual un usuario ingresa al sistema con su usuario correspondiente (anteriormente debe ser creado por el administrador del sistema) donde podrá realizar operaciones de Altas, Modificaciones y Bajas de mesas reservadas. 
</p>

<h3 align="center">¿Cómo instalar y correr el sistema?</h3>

<p align="center">
    Ejecutar en la consola las siguientes instrucciones
</p>
<p>
    python manage.py makemigrations reservas
    python manage.py migrate
    python manage.py createsuperuser (indicando username, email y password del admin) username=pruebaadmin password=prueba123 username=roberto password=prueba123
    python manage.py runserver (Dirigirse al link especificado)
</p>

<p>
    Dentro de la ruta /admin/ con el admin logueado. Se podrá crear nuevos usuarios desde la ruta users. Para crear un nuevo cliente se deberá asociarlo a un usuario registrado del sistema, para que este pueda loguearse y realizar las diferentes operaciones disponibles.
    
    El admin será el encargado de crear, modificar y eliminar las mesas para su posterior reserva, Desde la ruta Mesas especificando si la mesa está ocupada o no y asociando esta mesa a un cliente si asi lo desea. Deberá agregar una descripción (EJ: posición de la mesa).

    Dentro de la ruta reservas el cliente podrá realizar altas, bajas y modificaciones sobre sus reservas.

    Obs: al desloguear un cliente y volver a ingresar se deberá verificar la url, esta tiene que ser: "/accounts/login/"
</p>

<p>
    Este proyecto se realizó como finalización del curso Django, un framework para el desarrollo de sitios web. Se pedía una aplicación web que permita realizar Altas, Bajas y Modificaciones sobre entidades.
</p>

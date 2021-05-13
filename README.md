#CONFIGURACIÓN

##Cree un entorno virtual:
```
python3 -m venv "nombre_entorno"

cd /.../ruta_entorno/mi_entorno
```
##Clonar el repositorio:
```
git clone "https://github.com/JohnKTB/Sistema-Inventario-Back.git"
```
##Activar entorno virtual:
```
source bin/activate
```
##Instalar dependencias:
```
pip install -r requirements.txt

cd mi_proyecto/
```
##TUTORIAL

####Settings
Abrir el archivo local.py que está dentro de la carpeta "settings" y reemplazar los campos ```NAME, USER y PASSWORD``` por los propios.

Crear un superusuario ```python manage.py createsuperuser``` y luego ejecutar ```python manage.py runserver```

####Asignar permisos

Navegar hasta ```http://127.0.0.1:8000/admin/```

Irse a "groups", crear un grupo y asignarle todos los permisos. Por último , irse a "users" y asignar el grupo creado al superusuario




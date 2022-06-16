"# miProyectoPy" 
https://github.com/germanTuppo/miProyectoPy.git
django-admin startproject miProyectoPy
python manage.py startapp miFamilia
crear modelos e insertar la aplicacion en settings
python manage.py makemigrations (con esto se crea base de datos, vacia de momento.)

Para meter las tablas: python manage.py sqlmigrate miFamilia 0001 esto crea la sentencia sql que crea la tabla y con pytho manage.py migrate las crea en el archivo db.sqlite3

Los elementos de la db los voy a crear a mano para el desafío, por lo menos algunos (despues ver poner mas con código)

Panel de administracion: python manage.py createsuperuser
User: germantuppo
Mail: germantuppo@gmail.com
pass: 836712839

cree las vistas y me copie los archivos que hizo el profe para ir probando. No me gusta la idea de copiarme una plantilla pero de momento vaaa!



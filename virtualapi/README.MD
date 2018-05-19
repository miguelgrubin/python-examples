# Instalar

- Instalar el paquete en tu python3 nativo
```
	pip3 install virtualenv
```
- Moverte al directorio base del proyecto.
- Crear un virtualenv
```
	virtualenv venv
```
- Activar el entorno virtual para instalar las dependencias
```
	source venv/bin/activate
```
- Ahora instalar las dependencias
```
	pip install -r requirements.txt
```
- Una vez instaladas las dependencias se han creado los ejecutables de gunicorn y flask que hay que hacer relativos
- Salimos del entorno virtual (Control + C o abrir otra terminal)
- Pasamos los ejecutables del entorno virtual a relativos para que se pueda mover la carpeta a futuro
```
	virtualenv --relocatable venv
```

# Configurar gunicorn y flask
Conf general de Gunicorn `./gunicorn.conf.py`
Conf general de Flask `./virutalapi/config.py`
Conf logging de Flask `./virutalapi/factory.py`


# Arrancar Servicio
```
./venv/bin/gunicorn -c gunicorn.conf.py srvapi:app
```
o
```
./start-server.py
```

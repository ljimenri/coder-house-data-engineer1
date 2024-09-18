
# Tercera Pre Entrega Data Engineer

Crear un Script liviano y funcional que pueda ser utilizado en cualquier Sistema operativo y por cualquier usuario. 

Dockerizar un Script para hacerlo funcional en cualquier sistema operativo. 






##  Ejecución Del Proyecto
Para levantar el proyecto ejecutar el siguiente comando en la carpeta raiz:

```bash
docker compose up
```
Observación 1: Me ocurrió en una oportunidad que los logs no mostraban la contraseña para ingresar a la consola de Airflow, se soluciona haciendo re intentos de login.
Observación 2: Se utilizó el siguiente correo andru.ocatorres@gmail.com como mail de destino para el envío de alertas, en caso de querer modificarlo se tiene que agregar en el archivo 

```bash
.env
```

en la linea que define la variable EMAIL_TO_ADDRESS

```bash
EMAIL_TO_ADDRESS=nuevo_mail
```

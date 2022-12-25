Gorka Cidoncha Marquiegui
Instalar gCloud y kubectl.
Tener un projecto creado con recurso necesarios para la creación de un cluster.
Crear un cluster gke-autopilot si no se tiene uno craeado con:
gcloud container clusters create-auto <cluster_name> --region <region>  --project=<project_ID>

Descargar la carpeta, y entrar en ella.
Ejecutar exec.sh con:
sh exec.sh

Para ver los contenedores creados o en proceso de creación:
get pods
Esperar a que todos lo contenedores se hayan creado.

Abrir un cliente mySql con:
kubectl run -it --rm --image=mysql --restart=Never mysql-client -- mysql --host mysql --password=pass
Puede que salte el error de timeout, si es asi espera unos minutos y vuelve a intentarlo.
Ejecutar los siguientes comandos en el cliente:
CREATE DATABASE myData;
USE myData;
CREATE TABLE messages(id INT PRIMARY KEY AUTO_INCREMENT, msg VARCHAR(255));

Para ver los servicios:
get services
Esperar a que el servicio "load balancer" tenga la ip-externa activa



Acceder a http://<ip-externa-del-servicio-"load-balancer">:5000/ en tu navegador.
El botón send mandara un mensaje con el texto introducido en la caja de texto superior.
El botón recive consumirá, guardara en la base de datos y mostrará todos los mensajes enviados que no hayan sido previamente consumidos.

Para ver los mensajes guardados en la base de datos acceder al cliente mySQL con:
kubectl run -it --rm --image=mysql --restart=Never mysql-client -- mysql --host mysql --password=pass
Ejecutar los siguientes comandos en el cliente:
USE myData;
SELECT * FROM messages;
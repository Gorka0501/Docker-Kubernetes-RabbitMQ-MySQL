Gorka Cidoncha Marquiegui
Instalar gCloud y kubectl.
Tener un proyecto creado con recurso necesarios para la creación de un cluster.
Crear un cluster si no se tiene uno creado con:
gcloud container clusters create-auto <cluster_name> --region <region>  --project=<project_ID>

Descargar la carpeta, y entrar en ella.
Ejecutar exec.sh con:
sh exec.sh

Para ver los contenedores creados o en proceso de creación:
get pods
Esperar a que todos lo contenedores se hayan creado.

Para ver los servicios:
get services
Esperar a que el servicio "load balancer" tenga la ip-externa activa



Acceder a http://<ip-externa-del-servicio-"load-balancer">:5000/ en tu navegador.
El botón send mandara un mensaje con el texto introducido en la caja de texto superior.
El botón recive consumirá y mostrará todos los mensajes enviados que no hayan sido previamente consumidos.

Gorka Cidoncha Marquiegui
Instalar Docker con snap intall docker
Descargar la carpeta, y entrar en ella.
Ejecutar este lista de comandos dentro de la carpeta:
sudo docker-compose up y esperar unos segundos a que el RabbitMQ arranque.
Para detenerlo
sudo docker-compose stop

Acceder a http://localhost:5000/ en tu navegador.
El botón send mandara un mensaje con el texto introducido en la caja de texto superior.
El botón recive consumirá y mostrará todos los mensajes enviados que no hayan sido previamente consumidos.
from flask import Flask, render_template, request
import pika
import os

app = Flask(__name__)

rabbitmq_user = os.getenv("RABBITMQ_DEFAULT_USER")
rabbitmq_pass = os.getenv("RABBITMQ_DEFAULT_PASS")

def send_msg(msg):
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    param = pika.ConnectionParameters("rabbitmq", credentials=credentials)
    connection = pika.BlockingConnection(param)
    channel = connection.channel()

    channel.queue_declare(queue='MSG')


    channel.basic_publish(exchange='', routing_key='MSG', body=msg)


    connection.close()
    return

def recive_msg():
    data = []
    credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_pass)
    param = pika.ConnectionParameters("rabbitmq", port=5672, credentials=credentials)
    connection = pika.BlockingConnection(param)
    channel = connection.channel()

    channel.queue_declare(queue='MSG')


    # Get ten messages and break out
    for method_frame, properties, body in channel.consume(queue='MSG', inactivity_timeout=1):
        
        if not (method_frame == None):
            # Display the message parts
            data.append(body)


            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            break
        

    # Close the channel and the connection
    channel.close()
    connection.close()
    return data
@app.route('/', methods=['POST', 'GET'])
def home():
    data=[]
    if request.method == "POST":
        if request.form['submit_button'] == 'Send':
            msg = request.form["msg"]
            send_msg(msg)

        if request.form['submit_button'] == 'Recive':
            data = recive_msg()

            
    
    return render_template('./index.html', data=data)

    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
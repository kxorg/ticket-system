from fastapi import FastAPI
import pika

app = FastAPI()


@app.get("/send_message")
def send_message(message_text: str): 
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('myrabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_publish(exchange='', routing_key='my_queue',
                          body=message_text)
    connection.close()
    return {"message": f'Message sent: "{message_text}"'}

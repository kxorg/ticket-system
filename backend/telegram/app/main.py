from fastapi import FastAPI
import pika

app = FastAPI()


# @app.get("/receive_message")
# def receive_message():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('myrabbitmq'))
#     channel = connection.channel()
#     method_frame, header_frame, body = channel.basic_get(queue='my_queue')
#     if method_frame:
#         message = body.decode("utf-8")
#         return {"message": message}
#     else:
#         return {"message": "No messages"}

from fastapi import FastAPI
import pika

app = FastAPI()

@app.get("/receive_message")
def receive_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('myrabbitmq'))
    channel = connection.channel()
    try:
        method_frame, header_frame, body = channel.basic_get(queue='my_queue')
        
        if method_frame:
            message = body.decode("utf-8")
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            
            return {"message": message}
    except:
        return {"message": "No messages"}

from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
import os
import logging
from dotenv import load_dotenv

load_dotenv(verbose=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
#@app.route('/webhook', methods=['POST'])
@app.route(os.environ["WEBHOOK_ROUTE"], methods=['POST'])
#@app.route('/', methods=['POST'])

def hello(): #hello() is registered to route /
    #Gets the POST body as a JSON object
    print(request.json)
    body = request.json

    #Bootstraps an instance of a Kafka producer.
    #Initializes the producer and identifies the docker server.
    #kafka-spotify is listed in /etc/hosts with the ip of the container
    #Sets the producer serializer to JSON
    producer = KafkaProducer(bootstrap_servers=os.environ["BOOTSTRAP_SERVER"],value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    #Send a message to the kafka topic 'test'
    #passes the POST JSON body as the message
    producer.send(os.environ["KAFKA_TOPIC"], body)
    #Closes the TCP stream to Kafka
    producer.close()
    #Returns a Complete string
    return "Complete"

if __name__ == '__main__':
#    app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=8001)

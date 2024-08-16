This is the repo explaining how I managed to build this container image.


It will probably seem silly but I can never remember the basic Podman commands so, here we go.

Under a Linux enviroment (in my case a RHEL8 EC2 instance in AWS that I"m using for development).

- assuming you already have PoDman installed.

- create a folder into which you put the requirements.txt / Dockerfile and kafka-consumer.py files

- then run

```
podman build --tag kafka-consumer .

podman push localhost/kafka-consumer:latest quay.io/USERNAME/FOLDER/kafka-consumer:latest
```

Both folders kafka-consumer and webhook-kafka represent each the folder structure to run the command above.

The repos here are:
 - kafka-consumer: [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/kafka-consumer) the repo to build the container doing the consuming/producing onto Kafka with data manipulation
 - wehook-kafka: [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/webhook-kafka) the repo to build the container doing webhook and producing onto Kafka the raw message (from ACS for example)
 - Test-kafka-consumer: [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/Test-kafka-consumer) the repo showing how to deploy and test via the OCP interface the kafka-consumer container
 - Test-webhook-kafka: [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/Test-webhook-kafka)  the repo showing how to deploy and test via the OCP interface the webhook-kafka container

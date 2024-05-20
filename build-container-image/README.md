This is the repo explaining how I managed to build this container image.

It will probably seem silly but I can never remember the commands so, here we go.

Under a Linux enviroment (in my case a RHEL8 EC2 instance in AWS that I"m using for development).

- assuming you already have PoDman installed.

- create a folder into which you put the requirements.txt / Dockerfile and kafka-consumer.py files

- than run

```
podman build --tag kafka-consumer .

podman push localhost/kafka-consumer:latest quay.io/USERNAME/FOLDER/kafka-consumer:latest
```

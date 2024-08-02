This folder contains the files for building the Container Image doing the webhook and kafka producer.

```
tree python-kafka/
python-kafka/
├── Dockerfile
├── kafka-consumer.py
└── requirements.txt

```

All 3 files are available in this folder. 
You then do the following

```

 podman build --tag kafka-consumer .
 podman login
 podman push localhost/kafka-consumer:latest quay.io/rhn_support_sdelord/kafka/kafka-consumer:latest

```

The container image is available at

```
podman pull quay.io/rhn_support_sdelord/kafka/kafka-consumer
```

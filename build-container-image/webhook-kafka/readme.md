This folder contains the files for building the Container Image doing the webhook and kafka producer.

```
tree webhook-python/
webhook-python/
├── Dockerfile
├── requirements.txt
└── webhook-kafka.py

```

All 3 files are available in this folder. 
You then do the following

```

 podman build --tag webhook-kafka .
 podman login
 podman push localhost/webhook-kafka:latest quay.io/rhn_support_sdelord/kafka/webhook-kafka:latest

```

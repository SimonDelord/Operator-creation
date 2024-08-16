

## step 1 - build container images

### video 1 build first container
```
tree python-ctner1
cd python-ctner1

podman build --tag python-ctner1 .
podman login
podman push localhost/python-ctner1:latest quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest

podman pull quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest
```

### video 2 build second container
```
tree python-ctner2
cd python-ctner2

podman build --tag python-ctner2 .
podman login
podman push localhost/python-ctner2:latest quay.io/rhn_support_sdelord/operator-demo/python-ctner2:latest

podman pull quay.io/rhn_support_sdelord/operator-demo/python-ctner2:latest
```

### video 3 

It shows the Kafka environment on ROSA and how to make the container images public on Quay.io

### video 4


It shows how to deploy the container images manually on Openshift and check the logs for each
```
container-1 

quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest
KAFKA_TOPIC acs-topic
KAFKA_TOPIC_2 eda-topic
BOOTSTRAP_SERVER 172.30.175.248:9092

container-2 

quay.io/rhn_support_sdelord/operator-demo/python-ctner2:latest
KAFKA_TOPIC acs-topic
BOOTSTRAP_SERVER 172.30.175.248:9092
WEBHOOK_ROUTE /webhook
```
Test by using Postman
curl -X POST http://webhook-kafka-simon-demo.apps.rosa-mw5w8.9knj.p1.openshiftapps.com/webhook -H "Content-type:application/json" -d '{"username":"simon","password":"garlic"}'
```

## step 1 - build container images


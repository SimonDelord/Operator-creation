This is the repo that is now trying to create a helm chart to deploy the container image created the kafka-consumer folder.

the first step is to wrap the Container Image created in a previous step into a Kubernetes object (typically a Deployment).

As part of the Deployment I'm configuring Environment Variables (e.g KAFKA_TOPIC, KAFKA_TOPIC_2, BOOTSTRAP_SERVER) as per the code below

```
hello

```

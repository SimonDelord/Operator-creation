This is the repo for the Kafka Consumer Container Image that will "wrapped" as an operator.

I am reusing the image I created for the ACS-Kafka-demo see here.

This image is currently sitting in quay.io and is publically available.

quay.io/rhn_support_sdelord/kafka/kafka-consumer

As part of the build it is possible to specify 3 parameters:

- BOOTSTRAP_SERVER - this is the endpoint for talking to the Kafka Broker
- KAFKA_TOPIC - this is the topic onto which this Container is going to listen/consume
- KAFKA_TOPIC_2 - this is the topic onto whic this Container is going to produce

The defaults are respectively - 172.30.113.193:9092 / acs-topic-5 / eda-topic

So an example of deploying this container onto OpenShift would be - see the screenshot below

Go into Developer View -> Add -> Container Image

Then paste the url for the container image (here - quay.io/rhn_support_sdelord/kafka/kafka-consumer)

Then click on Deployment where "Click on the names to access advanced options for Health checks, Deployments, Scaling, Resource limits and Labels to add the variables.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/kafka-consumer/images/Creating-From-container-image-1.png)
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/kafka-consumer/images/Creating-From-container-image-2.png)

<p align=center>  Deploying the Container Image from OCP Console </p>



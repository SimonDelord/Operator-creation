This is the repo for the Python Webhook Container Image that will "wrapped" as an operator.

I am reusing the image I created for the ACS-Kafka-demo see here.

This image is currently sitting in quay.io and is publically available.

quay.io/rhn_support_sdelord/kafka/webhook-kafka

As part of the build it is possible to specify 3 parameters:

- BOOTSTRAP_SERVER - this is the endpoint for talking to the Kafka Broker
- KAFKA_TOPIC - this is the topic onto which this Container is going to produce
- WEBHOOK_ROUTE - this is the path for the webhook (consumable as a route)

The defaults are respectively 
- 172.30.113.193:9092
- acs-topic-5
- /webhook

So an example of deploying this container onto OpenShift would be - see the screenshot below

Go into Developer View -> Add -> Container Image

Then paste the url for the container image (here - quay.io/rhn_support_sdelord/kafka/webhook-kafka)

Then click on Deployment where "Click on the names to access advanced options for Health checks, Deployments, Scaling, Resource limits and Labels to add the variables.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/config-1.png)
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/config-2.png)
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/config-3.png)
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/config-4.png)


<p align=center>  Deploying the Container Image from OCP Console </p>


To test that the webhook is up and running you can run the following command
```
 curl -X POST https://<service-name>-<project-name>.apps.<cluster-name>.openshiftapps.com/webhook -H "Content-type:application/json" -d '{"name":"simon","password":"garlic"}

```
so in the example with the screenshots above
```
curl -X POST https://webhook-kafka-simon-demo.apps.rosa-2h58p.b3ox.p1.openshiftapps.com/webhook -H "Content-type:application/json" -d '{"name":"simon","password":"cheese"}'
```

which gives the following logs (before and after the curl command)

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/logs-before-curl.png)
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-container-image/Test-webhook-kafka/images/logs-after-curl.png)

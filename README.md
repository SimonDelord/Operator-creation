# Operator-creation
This is a repo showing how to create your own Operator using Helm

There are a set of folders / subfolders in here.

- build-container-image: shows how to simply build the Container Image using PodMan and push it to a repo (like quay.io)
- kafka-consumer: shows how to create the "container image" (E.g the various variables, files, etc...) so it can then be wrapped into a Helm chart
- helm-kafka: shows how to create the helm chart to deploy the container image defined in the kafka-consumer repo
- operator: shows then how to create the Operator based on the helm-chart in the previous repo
- ACM-configuration: shows then how to deploy/configure these operators using ACM Policies and Applications (with or without ArgoCD).



## The Problem Statement

As part of a previous demo built in collaboration with my colleagues Derek Waters and Shane Boulden, see [here](https://github.com/SimonDelord/ACS-Kafka-Demo-), we showed that it is possible to create two simple microservices to provide a simple way to integrate ACS and EDA for AAP via a Kafka layer. This is presented in the figure below.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Problem-Statement-Figure-1.png)

When we zoom in, we can see that the solution is made up of two different containers:
 - a webhook and kafka producer
 - a microservice that listens on a specific topic, does data manipulation and exports the new data onto a different topic.

This is presented in the figure below.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Problem-Statement-Figure-2.png)

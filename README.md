# Operator-creation
This is a repo showing how to create your own Operator using Helm

There are a set of folders / subfolders in here.

- build-container-image: shows how to simply build the Container Image using PodMan and push it to a repo (like quay.io)
- helm-kafka: shows how to create the helm chart to deploy the container image defined in the kafka-consumer repo
- operator-build: shows then how to create the Operator based on the helm-chart in the previous repo
- operator-bundle: shows how to create the catalog items for onboarding and deploying the operators created in the previous step
- ACM-configuration: shows then how to deploy/configure these operators using ACM Policies and Applications (with or without ArgoCD).



## The Problem Statement

As part of a previous demo built in collaboration with my colleagues Derek Waters and Shane Boulden, see [here](https://github.com/SimonDelord/ACS-Kafka-Demo-), we showed that it is possible to create two simple microservices to provide a simple way to integrate ACS and EDA for AAP via a Kafka layer. 

This is presented in the figure below.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Problem-Statement-Figure-1.png)

When we zoom in, we can see that the solution incorporates two "in-house" developed containers:
 - a webhook and kafka producer
 - a microservice that listens on a specific topic, does data manipulation and exports the new data onto a different topic.

This is presented in the figure below.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Problem-Statement-Figure-2.png)

Because, I am really not a developer, I simply hacked my way through some Python code and harcoded some values in each of these containers, which is not great.

Following that demo, I then realised that it would be a lot easier if I could simply make sure that those two functions I had created were made "more flexible" by providing:
 - build time configuration of the various parameters (e.g Kafka server address, Kafka topics, URL for the webhook)
 - run time monitoring of each these containers to make sure it could auto-correct / rebuild / scale / etc... based on specific metrics.

So, it seemed like Kubernetes Operators were the way to go to achieve both.
This "blog" / GitHub repo will then take you through all the steps I took to achieve the above.

## Overview - High sequence of steps & Environment

The following diagram shows the high level sequence of steps for creating and deploying your own operator (including a governance function using Red Hat ACM).

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Overview-Figure-1.png)

The next diagram shows the actual setup I used to do this (e.g you don't have to do the same, but I found it worked better this way for me).

<div align="center">
![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/images/Overview-Figure-2.png)
</div>

Each step is detailed in the following sections.

## First Step - Build the container images so it can receive variables at Run Time.

The first step of this demo is to build container images, the details around how to do it are:
 - in this folder for the general process using Podman [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image)
 - in this folder for the webhook container [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/webhook-kafka)
 - in this folder for the kafka consumer/producer container [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/kafka-consumer)

Once you have done this, you can then verify that these two images can be deployed on OpenShift:
 - in this folder, I have given an example on how to do it from the OpenShift console [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-container-image/Test-kafka-consumer)

## Second Step - Build a Helm Chart to deploy your container image and associated Kubernetes artefacts

As part of this step, we then try and automate the configuration and deployment of the container images using Helm Charts.
 - see [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-helm-charts) for the overall approach
 - see [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-helm-charts/helm-webhook) for the detailed helm chart for the webhook container image
 - see [here](https://github.com/SimonDelord/Operator-creation/tree/main/build-helm-charts/helm-kafka) for the detailed helm chart for the kafka consumer producer image

Once you have done this, you can verify that both charts deploy properly and run tests (and check the logs for each of the PoDs).
 - see here for the tests for the webhook (TBD)
 - see here for the tests for the kafka container image (TBD)


# Operator-creation
This is a repo showing how to create your own Operator using Helm

There are a set of folders / subfolders in here.

- build-container-image: shows how to simply build the Container Image using PodMan and push it to a repo (like quay.io)
- kafka-consumer: shows how to create the "container image" (E.g the various variables, files, etc...) so it can then be wrapped into a Helm chart
- helm-kafka: shows how to create the helm chart to deploy the container image defined in the kafka-consumer repo
- operator: shows then how to create the Operator based on the helm-chart in the previous repo
- ACM-configuration: shows then how to deploy/configure these operators using ACM Policies and Applications (with or without ArgoCD).

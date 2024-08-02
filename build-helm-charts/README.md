This is the repo that showing how to create a helm chart to deploy the container image(s) created the build-container-image folder.

I am trying to follow a sequence of steps:

- Define a deployment.yaml artefact passing the enviroment variables either directly as part of the deployment definition or using a configMap
- Create an helm chart around the deployment.yaml and configmap.yaml

In the folder helm-kafka (E.g for the consumer/producer container image) I explain both approaches and detail the various steps and files.
In the folder helm-webhook, I go directly with the configmap approach (e.g no need to reexplain everything).

So the structure here is:
- helm-kafka: folder for helm chart of the kafka consumer/producer container image
- helm-webhook: folder for the helm chart of the webhook / kafka producer container image

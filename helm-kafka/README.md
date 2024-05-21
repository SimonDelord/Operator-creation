This is the repo that is now trying to create a helm chart to deploy the container image created the kafka-consumer folder.

I am trying to follow a sequence of steps:

- Define a deployment.yaml artefact passing the enviroment variables either directly as part of the deployment definition or using a configMap
- Create an helm chart around the deployment.yaml and configmap.yaml

### Step 1 - Create a Deployment.yaml and ConfigMap.yaml artefacts

The first step is to wrap the Container Image created in a previous step into a Kubernetes object (typically a Deployment).

As part of the Deployment I'm configuring Environment Variables (e.g KAFKA_TOPIC, KAFKA_TOPIC_2, BOOTSTRAP_SERVER) as per the code below

```
    spec:
      containers:
        - name: basic-kafka-consumer
          image: >-
            quay.io/rhn_support_sdelord/kafka/kafka-consumer
          env:
          - name: KAFKA_TOPIC
            value: acs-topic-6
          - name : KAFKA_TOPIC_2
            value: acs-topic-5
          ports:
            - containerPort: 8001
              protocol: TCP

```
The snippet above is an extract from the deployment-kafka-with-variables.yaml file in this folder

The next iteration is to use a configmap and reference this configMap in the Deployment.yaml

See the snippet below showing both the mapping in the deploymeny.yaml and the configmap.yaml.

Both files are available in this repo under the names - deployment-kafka-with-configmap.yaml and kafka-configmap.yaml

```

    spec:
      containers:
        - name: basic-kafka-consumer-configmap
          image: >-
            quay.io/rhn_support_sdelord/kafka/kafka-consumer
          env:
          - name: KAFKA_TOPIC
            valueFrom:
              configMapKeyRef:
                name: kafka-configmap
                key: KAFKA_TOPIC_KEY
          - name : KAFKA_TOPIC_2
            valueFrom:
              configMapKeyRef:
                name: kafka-configmap
                key: KAFKA_TOPIC_2_KEY
          - name: BOOTSTRAP_SERVER
            valueFrom:
              configMapKeyRef:
                name: kafka-configmap
                key: BOOTSTRAP_SERVER_KEY
          ports:
            - containerPort: 8001
              protocol: TCP


======================================

apiVersion: v1
kind: ConfigMap
metadata:
  name: kafka-configmap
  namespace: simon-demo-2
data:
  KAFKA_TOPIC_KEY: acs-topic-6
  KAFKA_TOPIC_2_KEY: acs-topic-5
  BOOTSTRAP_SERVER_KEY: 172.30.113.193:9092

```


### Step 2 - Create a Helm Chart based of the Deployment and ConfigMap files


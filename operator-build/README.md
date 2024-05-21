This is the repo describing how to build the Operator based on the Helm chart created in the previous step
```
mkdir webhook-kafka-operator
cd webhook-kafka-operator/
export OPERATOR_NAME=webhook-kafka
export OPERATOR_PROJECT=webhook-kafka-operator-project
export OPERATOR_VERSION=v1.0.0
export DOCKER_USERNAME=rhn_support_sdelord
export IMAGE=quay.io/${DOCKER_USERNAME}/${OPERATOR_NAME}:${OPERATOR_VERSION}
mkdir -p ${OPERATOR_PROJECT}

operator-sdk init --plugins=helm --domain frenchidiot.com --helm-chart-repo /home/ec2-user/Operator-SRE/helm-chart-kafka/simon-kafka/
operator-sdk create api --helm-chart=/home/ec2-user/Operator-SRE/helm-chart-kafka/simon-kafka/
docker login quay.io -u $DOCKER_USERNAME
make docker-build docker-push IMG=${IMAGE}
```
don't forget to make it visible in quay.io
```
cd webhook-kafka-operator-project/
make install

oc apply -f config/samples/charts_v1alpha1_simonkafka.yaml
```

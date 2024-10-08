

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
```
curl -X POST http://webhook-kafka-simon-demo.apps.rosa-mw5w8.9knj.p1.openshiftapps.com/webhook -H "Content-type:application/json" -d '{"username":"simon","password":"garlic"}'
```

## step 2 - build helm chart

### video 1 build the chart
show how to build helm charts

```
helm create helm-python-ctner1
tree helm-python-ctner1

```

### video 2 show the tree structure and deploy to openshift
show the tree structure once all files have been modified

```
tree helm-python-ctner1
helm install helm-python-ctner1 ./helm-python-ctner1/helm-python-ctner1/

tree helm-python-ctner2
helm install helm-python-ctner2 ./helm-python-ctner2/helm-python-ctner2/

helm list
```

and then you show podman to curl this stuff


### video 3 show both helm charts deployed and test them

show in the openshift console both helm chart deployed
show postman to curl this stuff and the logs on the PoDs


## step 3 build operators using sdk
### video 1 - build operator for ctner1 using operator-sdk

```
export OPERATOR_NAME=op-python-ctner1
export OPERATOR_PROJECT=op-python-ctner1
export OPERATOR_VERSION=v1.0.0
export DOCKER_USERNAME=rhn_support_sdelord
export IMAGE=quay.io/${DOCKER_USERNAME}/${OPERATOR_NAME}:${OPERATOR_VERSION}
mkdir -p ${OPERATOR_PROJECT}

cd ${OPERATOR_PROJECT}
operator-sdk init --plugins=helm --helm-chart-repo /home/ec2-user/Operator-SRE/helm-charts-videos-youtube/helm-python-ctner1/helm-python-ctner1/
operator-sdk create api --helm-chart=/home/ec2-user/Operator-SRE/helm-charts-videos-youtube/helm-python-ctner1/helm-python-ctner1/
```

### video 2 - push the container image of the operator to quay
```
make docker-build docker-push IMG=${IMAGE}
```
make it visible in quay
```
make install
make deploy IMG=${IMAGE}
```
you now have one control manager running in its own namespace

### video 3 - deploy one instance of this operator and start fucking around with it

```
ls
tree config/
go into the logs of the operator

oc apply -f config/samples/charts_v1alpha1_helmpythonctner1.yaml
```
start to scale up and down

```
make undeploy
```

### video 4 - show both operators running and two instances running too



## Step 4 - Do the Operator Bundle

### video 1 - use the operator SDK to create the bundle

```
export IMG=quay.io/rhn_support_sdelord/op-python-ctner2:v1.0.0
export BUNDLE_IMG=quay.io/rhn_support_sdelord/op-python-ctner2-bundle

make bundle

tree bundle
```

### video 2 show the "icon" and then build this operator

```
make bundle-build bundle-push
```
make it visible in Quay

```
operator-sdk bundle validate $BUNDLE_IMG
operator-sdk run bundle quay.io/rhn_support_sdelord/op-python-ctner2-bundle:latest
```

### video 3 Do a manual setup of the automated view before - first step is the CatalogFile and associated ContainerImage

show the various files - CatalogFile
Get onto the RHEL8 jumphost
```
mkdir -p python-ctner1-catalog/python-ctner2-operator
opm generate dockerfile python-ctner2-catalog

vi python-ctner2-catalog.yaml

Schema: olm.semver
GenerateMajorChannels: true
GenerateMinorChannels: false
Stable:
  Bundles:
  - Image: quay.io/rhn_support_sdelord/op-python-ctner2-bundle:latest

opm alpha render-template semver -o yaml < python-ctner2-catalog.yaml > python-ctner2-catalog/catalog.yaml
opm validate python-ctner2-catalog
echo $?

podman build . -f python-ctner2-catalog.Dockerfile -t quay.io/rhn_support_sdelord/python-ctner2-catalog:latest
podman push quay.io/rhn_support_sdelord/python-ctner2-catalog:latest
```

### video 4 - create the catalog Source
create the catalog source on the normal jumphost (Simon's jumphost) and do this
```
vi catalog-source-op-python-ctner2.yaml

apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  annotations:
    operators.operatorframework.io/index-image: 'quay.io/operator-framework/opm:latest'
  name: python-ctner2-catalog
  namespace: simon-demo
spec:
  displayName: python-ctner2-catalog
  grpcPodConfig:
    securityContextConfig: legacy
  publisher: operator-sdk
  image: quay.io/rhn_support_sdelord/python-ctner2-catalog:latest
  secrets:
    - ''
  sourceType: grpc
```
amd then deploy it
```
oc apply -f catalog-source-op-python-ctner2.yaml
```

### video 5 - deplyo the subscription

show the subscription and then deploy it

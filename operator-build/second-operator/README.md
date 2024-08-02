This is the repo describing how to build the Operator based on the webhook-kafka helm chart.
```
export OPERATOR_NAME=web-simon
export OPERATOR_PROJECT=web-simon-project
export OPERATOR_VERSION=v1.0.0
export DOCKER_USERNAME=rhn_support_sdelord
export IMAGE=quay.io/${DOCKER_USERNAME}/${OPERATOR_NAME}:${OPERATOR_VERSION}
mkdir -p ${OPERATOR_PROJECT}

operator-sdk init --plugins=helm --helm-chart-repo /home/ec2-user/Operator-SRE/helm-chart-25-07-24/webhook-kafka/
operator-sdk create api --helm-chart=/home/ec2-user/Operator-SRE/helm-chart-25-07-24/webhook-kafka/

docker login quay.io -u $DOCKER_USERNAME
make docker-build docker-push IMG=${IMAGE}
```
don't forget to make it visible in quay.io
then you deploy the operator
```
cd webhook-kafka-operator-project/
you may have to create a set of roles or grand them rights
ok there are multiple "tweaks" I had to do to get this shit running

first tweak -
need to give proper permissions in the rbac folder 
otherwise this will fuck up your deployments, I just couldn't be fucked looking for which CRUD commands were making it impossible to deploy, so I simply took the cluster-admin role (here you go).
so in config/rbac/role.yaml

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    app.kubernetes.io/name: clusterrole
    app.kubernetes.io/instance: manager-role
    app.kubernetes.io/component: rbac
    app.kubernetes.io/created-by: simon-op
    app.kubernetes.io/part-of: simon-op
    app.kubernetes.io/managed-by: kustomize
  name: manager-role
rules:
  - verbs:
      - '*'
    apiGroups:
      - '*'
    resources:
      - '*'
  - verbs:
      - '*'
    nonResourceURLs:
      - '*'
```
Next!!!
change the default memory/cpu allocations for the Operator deployment (again not sure why they're so low, makes no sense).
so in 
config/default/manager_auth_proxy_patch.yaml
configu/manager/manager.yaml

change memory to 4Gi and cpu to 1 for example


```
make install  (be sure to be in the folder where there is a MakeFile to run this command, so you may have to go back one up)....
make deploy IMG=${IMAGE}
```

```
Then you can start deploying instances of the "operator"

```
oc apply -f config/samples/charts_v1alpha1_simonkafka.yaml
```
when you need to remove everything do

```
make undeploy
```

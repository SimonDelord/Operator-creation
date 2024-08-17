Repo for the videos I'm doing on the Operator stuff.

## Step 1
First you create a couple of variables representing the operator you created in the previous step
for me it was op-python-ctner1:v1.0.0 and then an associated "Bundle image" (e.g the image used by OLM).

```
export IMG=quay.io/rhn_support_sdelord/op-python-ctner1:v1.0.0
export BUNDLE_IMG=quay.io/rhn_support_sdelord/op-python-ctner1-bundle
```

then you do the following
```
make bundle
```
This will go and create a set of files similar to this

```
tree bundle
bundle
├── manifests
│   ├── charts.my.domain_helmpythonctner1s.yaml
│   ├── op-python-ctner1.clusterserviceversion.yaml
│   ├── op-python-ctner1-controller-manager-metrics-service_v1_service.yaml
│   └── op-python-ctner1-metrics-reader_rbac.authorization.k8s.io_v1_clusterrole.yaml
├── metadata
│   └── annotations.yaml
└── tests
    └── scorecard
        └── config.yaml
```

then you can go and modify the icon in the bundle/manifests/op-python-ctner1.clusterserviceversion.yaml

```
make bundle-build bundle-push #this push the Container Image of the Operator Bundle into Quay.io"
operator-sdk bundle validate $BUNDLE_IMG
operator-sdk run bundle quay.io/rhn_support_sdelord/op-python-ctner1-bundle:latest
(if you do the command above without the version it seems to fuck up). 
```
make sure you don't forget to open up the visibility on the container registry

```
operator-sdk run bundle quay.io/rhn_support_sdelord/op-python-ctner1-bundle:latest
INFO[0009] Creating a File-Based Catalog of the bundle "quay.io/rhn_support_sdelord/op-python-ctner1-bundle:latest"
INFO[0010] Generated a valid File-Based Catalog
INFO[0032] Created registry pod: quay-io-rhn-support-sdelord-op-python-ctner1-bundle-latest
INFO[0033] Created CatalogSource: op-python-ctner1-catalog
INFO[0033] OperatorGroup "operator-sdk-og" created
INFO[0033] Created Subscription: op-python-ctner1-v0-0-1-sub
INFO[0076] Approved InstallPlan install-n25n5 for the Subscription: op-python-ctner1-v0-0-1-sub
INFO[0076] Waiting for ClusterServiceVersion "simon-demo/op-python-ctner1.v0.0.1" to reach 'Succeeded' phase
INFO[0077]   Waiting for ClusterServiceVersion "simon-demo/op-python-ctner1.v0.0.1" to appear
INFO[0078]   Found ClusterServiceVersion "simon-demo/op-python-ctner1.v0.0.1" phase: Pending
INFO[0080]   Found ClusterServiceVersion "simon-demo/op-python-ctner1.v0.0.1" phase: Installing
INFO[0092]   Found ClusterServiceVersion "simon-demo/op-python-ctner1.v0.0.1" phase: Succeeded
INFO[0092] OLM has successfully installed "op-python-ctner1.v0.0.1"
```

### manual setup
The manual setup of on-boarding the operator into the catalog is the following:

 - create a CatalogFile (either via Raw Catalog Files or using the Catalog File template) and via the opm cli create a container image of this catalog file and point your catalogSource towards it
 - create a catalogSource (and point it to the image that was created in the previous step)
 - create a subscription (e.g as a way of installing the operator bundle)

## Create the catalog File
connect onto the RHEL8 jumphost

```
mkdir -p python-ctner1-catalog/python-ctner1-operator
opm generate dockerfile python-ctner1-catalog/
```

then create the catalog file 
```
$ cat simon-catalog.yaml
Schema: olm.semver
GenerateMajorChannels: true
GenerateMinorChannels: false
Stable:
  Bundles:
  - Image: quay.io/rhn_support_sdelord/op-python-ctner1-bundle:latest
```
```
opm alpha render-template semver -o yaml < python-ctner1-catalog.yaml > python-ctner1-catalog/catalog.yaml

$ opm validate python-ctner1-catalog
$ echo $?
0
```
Then build the image and push it to quay
```
podman build . -f python-ctner1-catalog.Dockerfile -t quay.io/rhn_support_sdelord/python-ctner1-catalog:latest
podman push quay.io/rhn_support_sdelord/python-ctner1-catalog:latest
```

## Create the Catalog Source
Back to the main jumphost (e.g simon's jumphost)

create a source catalog file - called catalog-source-op-python-ctner1.yaml
```
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  annotations:
    operators.operatorframework.io/index-image: 'quay.io/operator-framework/opm:latest'
  name: python-ctner1-catalog
  namespace: simon-demo
spec:
  displayName: python-ctner1-catalog
  grpcPodConfig:
    securityContextConfig: legacy
  publisher: operator-sdk
  image: quay.io/rhn_support_sdelord/python-ctner1-catalog:latest
  secrets:
    - ''
  sourceType: grpc
```

you simply deploy it
```
oc apply -f catalog-source-op-python-ctner1.yaml
catalogsource.operators.coreos.com/python-ctner1-catalog created
```
wait a few seconds and the icon should appear in the Operator Hub.

## Create the Subscription
you then need to create the subcription (e.g it's the deployment of the Operator from the Catalog to a specific namespace)

```
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: op-python-ctner1
  namespace: simon-demo
spec:
  channel: stable-v0
  installPlanApproval: Automatic
  name: op-python-ctner1
  source: python-ctner1-catalog
  sourceNamespace: simon-demo
  startingCSV: op-python-ctner1.v0.0.1
```
and then apply it

```
oc apply -f subscription-op-python-ctner1.yaml
```




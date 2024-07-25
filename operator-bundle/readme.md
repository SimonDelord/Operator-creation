This is the repo for all the "bundling" activities.
eg once the Operator has been created, we now need to put it into the OLM...


https://sdk.operatorframework.io/docs/olm-integration/quickstart-bundle/

```
export USERNAME=rhn_support_sdelord
export VERSION=0.0.1
export IMG=docker.io/$USERNAME/memcached-operator:v$VERSION // location where your operator image is hosted
export BUNDLE_IMG=docker.io/$USERNAME/memcached-operator-bundle:v$VERSION // location where your bundle will be hosted
```

then you do the following

```
make bundle
make bundle-build bundle-push #this push the Container Image of the Operator Bundle into Quay.io"
operator-sdk bundle validate $BUNDLE_IMG
operator-sdk run bundle $BUNDLE_IMG

```


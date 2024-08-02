This is the repo for all the "bundling" activities for the second Operator
eg once the Operator has been created, we now need to put it into the OLM...


https://sdk.operatorframework.io/docs/olm-integration/quickstart-bundle/

```
export IMG=quay.io/rhn_support_sdelord/web-simon
export BUNDLE_IMG=quay.io/rhn_support_sdelord/web-simon-bundle
```

then you do the following

```
make bundle
make bundle-build bundle-push #this push the Container Image of the Operator Bundle into Quay.io"
operator-sdk bundle validate $BUNDLE_IMG
operator-sdk run bundle $BUNDLE_IMG

```

make sure you don't forget to open up the visibility on the container registry

```

[root@ip-10-124-3-196 simon-op]# operator-sdk run bundle $BUNDLE_IMG
INFO[0009] Creating a File-Based Catalog of the bundle "quay.io/rhn_support_sdelord/simon-op-bundle:v1.0.0"
INFO[0010] Generated a valid File-Based Catalog
INFO[0016] Created registry pod: quay-io-rhn-support-sdelord-simon-op-bundle-v1-0-0
INFO[0016] Created CatalogSource: simon-op-catalog
INFO[0016] Created Subscription: simon-op-v1-0-0-sub
INFO[0054] Approved InstallPlan install-v9bxn for the Subscription: simon-op-v1-0-0-sub
INFO[0054] Waiting for ClusterServiceVersion "simon-demo/simon-op.v1.0.0" to reach 'Succeeded' phase
INFO[0055]   Waiting for ClusterServiceVersion "simon-demo/simon-op.v1.0.0" to appear
INFO[0056]   Found ClusterServiceVersion "simon-demo/simon-op.v1.0.0" phase: Pending
INFO[0058]   Found ClusterServiceVersion "simon-demo/simon-op.v1.0.0" phase: Installing
INFO[0069]   Found ClusterServiceVersion "simon-demo/simon-op.v1.0.0" phase: Succeeded
INFO[0070] OLM has successfully installed "simon-op.v1.0.0"

```

```
 tree bundle
bundle
├── manifests
│   ├── charts.my.domain_simonkafkas.yaml
│   ├── simon-op.clusterserviceversion.yaml
│   ├── simon-op-controller-manager-metrics-service_v1_service.yaml
│   └── simon-op-metrics-reader_rbac.authorization.k8s.io_v1_clusterrole.yaml
├── metadata
│   └── annotations.yaml
└── tests
    └── scorecard
        └── config.yaml

4 directories, 6 files
```

The manual setup of on-boarding the operator into the catalog is the following:
- create a CatalogFile (either via Raw Catalog Files or using the Catalog File template) and via the opm cli create a container image of this catalog file and point your catalogSource towards it
- create a catalogSource (and point it to the image that was created in the previous step)
- create a subscription (e.g as a way of installing the operator bundle)

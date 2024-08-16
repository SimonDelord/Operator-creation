

## step 1 - build container images

### video 1 build first container
```
tree python-ctner1
cd python-ctner1

podman build --tag python-ctner1 .
podman login
podman push localhost/kafka-consumer:latest quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest

podman pull quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest
```

### video 2 build second container
```
tree python-ctner2
cd python-ctner2

podman build --tag python-ctner2 .
podman login
podman push localhost/kafka-consumer:latest quay.io/rhn_support_sdelord/operator-demo/python-ctner2:latest

podman pull quay.io/rhn_support_sdelord/operator-demo/python-ctner2:latest
```

### video 3 

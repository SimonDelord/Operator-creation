

```
tree python-ctner1
cd python-ctner1

podman build --tag python-ctner1 .
podman login
podman push localhost/kafka-consumer:latest quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest

podman pull quay.io/rhn_support_sdelord/operator-demo/python-ctner1:latest
```

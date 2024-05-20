FROM registry.access.redhat.com/ubi8/ubi-minimal

RUN \
  microdnf install \
  net-tools bind-utils iputils curl git unzip vim wget podman yum\
  && microdnf clean all

RUN wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/openshift-client-linux-4.15.13.tar.gz
RUN tar -xvzf openshift-client-linux-4.15.13.tar.gz

ENV HOME /root

WORKDIR /root

CMD tail -f /dev/null

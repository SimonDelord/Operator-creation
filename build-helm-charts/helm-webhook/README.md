This is the repo that is now trying to create a helm chart to deploy the container image created in the build-container-image/webhook-kafka folder.

### Step 1 - Create the various files for the Helm Template and the helm chart

```
helm create webhook-kafka
```

Remove unnecessary files. The final structure should look like the following

```
tree webhook-kafka/
webhook-kafka/
├── charts
├── Chart.yaml
├── templates
│   ├── deployment.yaml
│   ├── _helpers.tpl
│   ├── route.yaml
│   ├── service.yaml
│   └── webhook-configmap.yaml
└── values.yaml

```

All the files are in the webhook-kafka folder.


```

You are then able to deploy your helm chart using the following command

```
 helm install webhook ./webhook-kafka/
```

You can test that the webhook is working by using the following command

```
curl -X POST http://webhook-kafka-simon-demo.apps.rosa-mw5w8.9knj.p1.openshiftapps.com/webhook -H "Content-type:application/json" -d '{"username":"simon","password":"garlic"}'

```
and check the logs on the PoD

```
INFO:kafka.conn:Set configuration api_version=(2, 5, 0) to skip auto check_version requests on startup
INFO:kafka.conn:<BrokerConnection node_id=2 host=my-cluster-kafka-2.my-cluster-kafka-brokers.simon-kafka.svc:9092 <connecting> [IPv4 ('10.131.2.93', 9092)]>: connecting to my-cluster-kafka-2.my-cluster-kafka-brokers.simon-kafka.svc:9092 [('10.131.2.93', 9092) IPv4]
INFO:kafka.conn:<BrokerConnection node_id=2 host=my-cluster-kafka-2.my-cluster-kafka-brokers.simon-kafka.svc:9092 <connecting> [IPv4 ('10.131.2.93', 9092)]>: Connection complete.
INFO:kafka.conn:<BrokerConnection node_id=bootstrap-0 host=172.30.156.161:9092 <connected> [IPv4 ('172.30.156.161', 9092)]>: Closing connection.
INFO:kafka.conn:<BrokerConnection node_id=2 host=my-cluster-kafka-2.my-cluster-kafka-brokers.simon-kafka.svc:9092 <connected> [IPv4 ('10.131.2.93', 9092)]>: Closing connection.
INFO:werkzeug:10.130.2.9 - - [02/Aug/2024 07:16:55] "POST /webhook HTTP/1.1" 200 
```

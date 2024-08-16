This is the repo showing how you can test both helm charts.

you would deploy both helm charts

```
helm create helm-kafka ./helm-kafka/
helm create helm-webhook ./helm-webhook/
```
you can then check that both charts have been deployed
```
helm list
```

and then you can use Postman to query both containers.

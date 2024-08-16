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

Here are a couple of screenshots showing the successful deployment of the charts and then the "curl" message via Postman.

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-helm-charts/test-helm-charts/images/helm-charts-deployed.png)

![Browser](https://github.com/SimonDelord/Operator-creation/blob/main/build-helm-charts/test-helm-charts/images/postman-screenshot.png)

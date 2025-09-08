You are requested to create the ingress name as critical-ingress to make the new application available at /pay.


Identify and implement the best approach to making this application available on the ingress controller and test to make sure its working.

Look into annotations: rewrite-target as well.

```yaml
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: critical-ingress
  namespace: critical-space
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "false"
spec:
  rules:
  - http:
      paths:
      - path: /pay
        pathType: Prefix
        backend:
          service:
           name: pay-service
           port:
            number: 8282
```
1. `minikube start --cpus=2 --memory=4096 --driver=docker`
2. `kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/standard-install.yaml`
3. `helm install eg oci://docker.io/envoyproxy/gateway-helm --version v1.4.1 -n envoy-gateway-system --create-namespace`
4. `kubectl wait --timeout=5m -n envoy-gateway-system deployment/envoy-gateway --for=condition=Available`

5. Create Gateway Class
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: my-gateway-class
spec:
  controllerName: example.com/gateway-controller # Replace with the actual controller name
```

We need to deploy Gateway Controller similar like ingress controller 
- Nginx Gateway: kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/gateway-api/main/config/crd/standard/gateway.networking.k8s.io_gatewayclasses.yaml

5. Create Gateway
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  gatewayClassName: my-gateway-class
  listeners:
  - protocol: HTTP
    port: 80
    name: http
```

5. Create HTTP Route
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: my-httproute
spec:
  parentRefs:
  - name: my-gateway
  hostnames:
  - "example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: my-service # Replace with your service name
      port: 8080 # Replace with your service port
```
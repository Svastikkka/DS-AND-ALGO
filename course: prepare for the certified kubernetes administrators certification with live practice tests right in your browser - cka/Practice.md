1. Create a `ClusterRole` named `pod-reader` that allows users to perform `get`, `list`, and `watch` operations on `pods`
```bash
  kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
```
2. Create a `ClusterRole` named `pod-reader` that only allows the `get` action on pods named `readablepod` and `anotherpod`.
```bash
kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod
```
3. Create a `ClusterRole` named `foo` that allows `get`, `list`, and `watch` operations on `replicasets` from the `apps` API group.
```bash
kubectl create clusterrole foo --verb=get --verb=list --verb=watch --resource=rs.apps
```
4. Create a `ClusterRole` named `foo` that allows `get`, `list`, and `watch` operations on `pods` and their `status` subresource.
5. Create a `ClusterRole` named `foo` that allows the `get` action on `non-resource URLs` under /logs/*.
6. Create a `ClusterRole` named `monitoring` that uses an aggregation rule with the label `rbac.example.com/aggregate-to-monitoring=true`.
7. Create a `ClusterRoleBinding` named `read-pods-binding` that binds the `pod-reader` `ClusterRole` to the user `alice`.
8. Create a `ClusterRoleBinding` named `multi-user-admin` that binds the `cluster-admin` `ClusterRole` to the users `bob` and `charlie`.
9. Create a `ClusterRoleBinding` named `qa-access` that binds the `edit` `ClusterRole` to users `qa1`, `qa2`, and the group `qa-team`.
10. Create a `ClusterRoleBinding` named `sa-monitoring` that binds the `view` `ClusterRole` to the `ServiceAccount` `monitor` in the `monitoring` namespace.
11. Create a `ConfigMap` named `my-config` from all the files inside the directory `/path/to/bar`.
12. Create a `ConfigMap` named `my-config` with custom keys `key1` and `key2` from files `/path/to/bar/file1.txt` and `/path/to/bar/file2.txt`
13. Create a `ConfigMap` named `my-config` with two literal values: `key1=config1` and `key2=config2`.
14. Create a `ConfigMap` named `my-config` from `key-value` pairs defined in the files inside `/path/to/bar`
15. Create a `ConfigMap` named `my-config` using environment variable definitions from the files `/path/to/foo.env` and `/path/to/bar.env`.
16. Create a `CronJob` named `my-job` schedule at `*/1 * * * *` with image `busybox`
17. Create a `CronJob` named `my-job` schedule at `*/1 * * * *` with image `busybox` with a command `date`
18. Create a `Deployment` named `testing` using the image `nginx`.
19. Create a `Deployment` named `testing` using the image `nginx` and configure it to run the command `sleep 1000`.
20. Create a `Deployment` named `testing` using the image `nginx` with `3` replicas.
21. Create a `Deployment` named `testing` using the image `nginx` and expose port `80`
22. Create a `Deployment` named `testing` that uses multiple images: `busybox:latest`, `ubuntu:latest`, and `nginx`
23. Create a single `Ingress` called `simple` that directs requests to `foo.com/bar` to the service `svc1:8080` with TLS enabled using secret `my-cert`.
24. Create a catch-all `Ingress` called `catch-all` that forwards traffic from `/path` to the service `svc1:8080`, and specify the Ingress Class as `otheringress`
25. Create an `Ingress` called `annotated` with Ingress Class `default`, routing traffic from `foo.com/bar` to `svc1:8080`, and add two annotations: `ingress.annotation1=foo` and `ingress.annotation2=bla`.
26. Create an `Ingress` called `multipath` with the same host `foo.com` but multiple paths: `/` to `svc1:8080` and `/admin/` to `svcadmin:8081` with ingress class name `default`
27. Create an `Ingress` called `ingress1` with multiple hosts: `foo.com/path*` forwarding to `svc:8080` and `bar.com/admin*` forwarding to `svc2:http`. Use pathType Prefix.
28. Create an `Ingress` called `ingtls` with Ingress Class `default`, TLS enabled using the `default` certificate, and two rules: `foo.com/` to `svc:8080` and `foo.com/path/subpath*` to `othersvc:8080`.
29. Create an `Ingress` called `ingsecret` with TLS enabled using secret `secret1`, host `foo.com/*` forwarding to `svc:8080`, and pathType `Prefix`.
30. Create an `Ingress` called `ingdefault` with a default backend `defaultsvc:http`, TLS enabled using `secret1`, and an additional rule forwarding `foo.com/*` to `svc:8080`.

31. Create a Pod with PVC and PV. [Refer Kubernetes Doc]()
32. Allow traffic only within the same namespace. Create a NetworkPolicy in namespace `testing` that allows pods to communicate only with other pods in the same namespace.
- Use podSelector: {} (all pods).
- Allow ingress only from namespaceSelector matching `testing`.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: access-nginx
  namespace: testing
spec:
  podSelector: {} # For ALL testing ns pods
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: testing
```
33. Deny all ingress traffic. In namespace `testing`, deny all inbound connections to all pods.
- Empty ingress: [] with podSelector: {}.
- policyTypes: ["Ingress"].
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: testing
spec:
  podSelector: {}  # For ALL testing ns pods
  policyTypes:
  - Ingress
  ingress: []
```
34. Allow traffic from specific pods. In namespace `backend`, allow ingress traffic only from pods with label `app: frontend`.
- podSelector for backend pods.
- ingress.from.podSelector.matchLabels.app: frontend.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
```
35. Allow egress only to a specific namespace. In namespace `space1`, allow pods labeled `app: app1` to send traffic only to pods in namespace `space2`.
- Use egress.to.namespaceSelector with kubernetes.io/metadata.name: space2.
- Add policyTypes: ["Egress"].
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: space1
spec:
  podSelector:
    matchLabels:
      app: app1
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: space2
```

36. Allow egress only to specific IP range. In namespace `monitoring`, allow all pods to reach external IP range `10.0.0.0/24`.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: monitoring
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24
```
37. Allow DNS access only. Create a policy in namespace `testing` to allow pods egress only to `kube-dns` service on port `53` (UDP/TCP).
- egress.ports.port: 53 with protocol: UDP and protocol: TCP.
- Add to.namespaceSelector for kube-system.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: testing
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: kube-system
    ports:
    - protocol: TCP
      port: 53
    - protocol: UDP
      port: 53
```

38. Allow frontend → backend on specific port. In namespace `testing`, allow pods with label `tier: frontend` to access `tier: backend` pods on port `8080`/TCP.

- podSelector for backend.
- ingress.from.podSelector.matchLabels.tier: frontend.
- ingress.ports.port: `8080`.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      tier: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          tier: frontend
    ports:
    - protocol: TCP
      port: 8080
```

39. Combine ingress + egress rules. In namespace `testing`, create a policy for pods labeled `role: data-processor` that:

- Allows ingress only from `role: collector`
- Allows egress only to `role: storage`
- Use both ingress and egress blocks.
- policyTypes: ["Ingress", "Egress"].

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: testing
spec:
  podSelector:
    matchLabels:
      role: data-processor
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          role: collector
  egress:
  - to:
    - podSelector:
        matchLabels:
          role: storage

```

40. Deny all egress except to external API. In namespace `testing`, deny all egress except to `35.201.0.0/16` on port `443` (HTTPS).
- Use ipBlock with except if you need to block subranges.
- Add ports.port: 443.
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: testing
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 35.201.0.0/16
    ports:
    - protocol: TCP
      port: 443
```

41. Allow access across namespaces using label. Allow pods in namespace `testing1` with label `team: alpha` to access pods labeled `team: beta` in namespace `testing2`.
- Use combination of podSelector (for backend pods) and namespaceSelector (for frontend-ns).
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: testing2
spec:
  podSelector:
    matchLabels:
      team: beta
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: testing1
      podSelector:
        matchLabels:
          team: alpha
```
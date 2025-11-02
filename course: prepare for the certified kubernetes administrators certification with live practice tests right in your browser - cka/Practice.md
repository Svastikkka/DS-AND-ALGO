1. Create a `ClusterRole` named `pod-reader` that allows users to perform `get`, `list`, and `watch` operations on `pods`
2. Create a `ClusterRole` named `pod-reader` that only allows the `get` action on pods named `readablepod` and `anotherpod`.
3. Create a `ClusterRole` named `foo` that allows `get`, `list`, and `watch` operations on `replicasets` from the `apps` API group.
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

31. Create a Pod with PVC and PV

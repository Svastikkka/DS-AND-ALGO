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


kubectl create ingress ingdefault --default-backend=defaultsvc:http  --rule="foo.com/*=svc:8080,tls=secret1"
kubectl create ingress ingdefault --default-backend=defaultsvc:http  --rule="foo.com/*=svc:8080,tls=secret1"

kubectl create ingress ingsecret --rule="foo.com/*=svc:8080,tls=secret1"

kubectl create ingress ingtls --class=default --rule="foo.com/=svc:8080,tls=default" --rule="foo.com/path/subpath*=othersvc:8080,tls=default"

kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:8081"
kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:8081"
kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:8081"
kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:8081"
kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:8081"

kubectl create ingress multipath --class=default --rule="foo.com/=svc1:8080" --rule="foo.com/admin/=svcadmin:8081"
kubectl create ingress multipath --class=default --rule="foo.com/=svc1=8080" --rule="foo.com/admin/=svcadmin:8081"
kubectl create ingress multipath --class=default --rule="foo.com/=svc1=8080" --rule="foo.com/admin/=svcadmin:8081"
kubectl create ingress multipath --class=default --rule="foo.com/=svc1=8080" --rule="foo.com/admin/=svcadmin:8081"
kubectl create ingress multipath --class=default --rule="foo.com/=svc1=8080" --rule="foo.com/admin/=svcadmin:8081"

kubectl create ingress annotated --class=default --rule="foo.com/bar=svc1:8080" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla
kubectl create ingress anootated --class=default --rule="foo.com/bar=svc1:8080" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla
kubectl create ingress annotated --class=default --rule="foo.com/bar=svc1:8080" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla
kubectl create ingress annotated --class=default --rule="foo.com/bar=svc1:8080" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla
kubectl create ingress annotated --class=default --rule="foo.com/bar=svc1:8080" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla

kubectl create ingress catch-all --class=otheringress --rule="/path=svc1:8080"
kubectl create ingress catch-all --class=otheringress --rule="/path=svc1:8080"
kubectl create ingress catch-all --class=otheringress --rule="/path=svc1:8080"
kubectl create ingress catch-all --class=otheringress --rule="/path=svc1:8080"
kubectl create ingress catch-all --class=otheringress --rule="/path=svc1:8080"

kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"
kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"
kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"
kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"
kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"

kubectl create deploy testing --image=busybox:latest --image=ubuntu:latest --image=nginx

kubectl create deploy testing --image=nginx --port=80

kubectl create deploy testing --image=nginx --replicas=3

kubectl create deploy testing --image=nginx -- sleep 1000

kubectl create deploy testing --image=nginx

kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox -- date

kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox
kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox
kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox
kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox
kubectl create cronjob my-job --schedule="*/1 * * * *" --image=busybox

kubectl create configmap my-config --from-env-file=/path/to/foo.env --from-env-file=/path/to/bar.env
kubectl create configmap my-config --from-env-file=/path/to/foo.env --from-env-file=/path/to/bar.env
kubectl create configmap my-config --from-env-file=/path/to/foo.env --from-env-file=/path/to/bar.env
kubectl create configmap my-config --from-env-file=/path/to/foo.env --from-env-file=/path/to/bar.env
kubectl create configmap my-config --from-env-file=/path/to/foo.env --from-env-file=/path/to/bar.env

kubectl create configmap my-config --from-file=key1=/path/to/bar
kubectl create configmap my-config --from-file=key1=/path/to/bar
kubectl create configmap my-config --from-file=key1=/path/to/bar
kubectl create configmap my-config --from-file=key1=/path/to/bar
kubectl create configmap my-config --from-file=key1=/path/to/bar

kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2
kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2
kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2
kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2
kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2

kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt
kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt
kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt
kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt
kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt


kubectl create configmap my-config --from-file=/path/to/bar
kubectl create configmap my-config --from-file=/path/to/bar
kubectl create configmap my-config --from-file=/path/to/bar
kubectl create configmap my-config --from-file=/path/to/bar
kubectl create configmap my-config --from-file=/path/to/bar

kubectl create clusterrolebinding sa-monitoring --cluster-role=view --serviceaccount=monitoring:monitor

kubectl create clusterrolebinding qa-access --clusterrole=edit --user=qa1 --user=qa2 --group=qa-team

kubectl create clusterrolebinding multi-user-admin --clusterrole=cluster-admin --user=bob --user=charlie

kubectl create clusterrolebinding read-pods-binding --clusterrole=pod-reader --user=alice
kubectl create clusterrolebinding read-pods-binding --clusterrole=pod-reader --user=alice
kubectl create clusterrolebinding read-pods-binding --clusterrole=pod-reader --user=alice
kubectl create clusterrolebinding read-pods-binding --clusterrole=pod-reader --user=alice
kubectl create clusterrolebinding read-pods-binding --clueterrole=pod-reader --user=alice

kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"


kubectl create clusterrole foo --verb=get --non-resource-url=/logs/*
kubectl create clusterrole foo --verb=get --non-resource-url=/logs/*
kubectl create clusterrole foo --verb=get --non-resource-url=/logs/*
kubectl create clusterrole foo --verb=get --non-resource-url=/logs/*
kubectl create clusterrole foo --verb=get --non-resource-url=/logs/*

kubectl create clusterrole foo --verb=get,list,watch --resources=pods,pods/status
kubectl create clusterrole foo --verb=get,list,watch --resources=pods,pods/status
kubectl create clusterrole foo --verb=get.list.watch --resources=pods,pods/ststus
kubectl create clusterrole foo --verb=get,list,watch --resources=pods,pods/status
kubectl create clusterrole foo --verb=get,list,watch --resources=pods,pods/status

kubectl create clusterrole foo --verb=get,list,watch --resources=replicasets.apps
kubectl create clusterrole foo --verb=get,list,watch --resources=replicasets.apps
kubectl create clusterrole foo --verb=get,list,watch --resources=replicasets.apps
kubectl create clusterrole foo --verb=get,list,watch --resources=replicasets.apps
kubectl create clusterrole foo --verb=get,list,watch --resources=replicasets.apps

kubectl create clusterrole pod-reader --verb=get --resource-name=readablepod --resource-name=anotherpod
kubectl create clusterrole pod-reader --verb=get --resource-name=readablepod --resource-name=anotherpod
kubectl create clusterrole pod-reader --verb=get --resource-name=readablepod --resource-name=anotherpod
kubectl create clusterrole pod-reader --verb=get --resource-name=readablepod --resource-name=anotherpod

kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods
kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods

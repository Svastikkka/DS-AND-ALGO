Create a new pod with the nginx image.
Create a new pod by creating manifest file
how many endpoint attach to svc


Pods
ReplicaSet





Get status of kubernetes composnents 
 kubectl get componentstatuses

cluster info
 kubectl cluster-info


Manually schedule the pod on node01. Delete and recreate the POD if necessary.
```
apiVersion: v1
kind: Pod
metadata:
  name: manual-pod
spec:
  containers:
    - name: nginx
      image: nginx
  nodeName: node01

```


kubectl get all



Create a taint on node01 with key of spray, value of mortein and effect of NoSchedule
```
kubectl taint node node01 spray=mortein:NoSchedule
```


```
apiVersion: v1
kind: Pod
metadata:
  name: bee
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "spray"
    operator: "Equal"
    value: "mortein"
    effect: "NoSchedule"
```

Remove the taint on controlplane, which currently has the taint effect of NoSchedule.

kubectl taint node controlplane node-role.kubernetes.io/control-plane:NoSchedule-


To learn spec of pod
```
kubectl explain pod.spec
kubectl explain pod.spec.tolerations

```

Apply a label color=blue to node node01

kubectl label nodes node01 color=blue


Set Node Affinity to the deployment to place the pods on node01 only.

kubectl explain deploy.spec.template.spec | grep -A10 affinity



Create a new deployment named red with the nginx image and 2 replicas, and ensure it gets placed on the controlplane node only.Use the label key - node-role.kubernetes.io/control-plane - which is already set on the controlplane node.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: red
spec:
  replicas: 2
  selector:
    matchLabels:
      app: red
  template:
    metadata:
      labels:
        app: red
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-role.kubernetes.io/control-plane
                operator: Exists
      containers:
      - name: nginx
        image: nginx
```


Deploy a DaemonSet for FluentD Logging.Use the given specifications.
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
    name: elasticsearch
spec:
    selector:
        matchLabels:
            name: elasticsearch
    template:
        metadata:
            labels:
                name: elasticsearch
        spec:
            containers:
                - name: elasticsearch
                  image: registry.k8s.io/fluentd-elasticsearch:1.20

```



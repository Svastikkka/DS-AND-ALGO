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


What is the path of the directory holding the static pod definition files?
Ans. /etc/kubernetes/manifests


Create a static pod named static-busybox that uses the busybox image , run in the default namespace and the command sleep 1000

```bash
kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml
```

Edit the image on the static pod you created in the previous task to use busybox:1.28.4
```bash
kubectl run --restart=Never --image=busybox:1.28.4 static-busybox --dry-run=client -o yaml --command -- sleep 1000 > /etc/kubernetes/manifests/static-busybox.yaml

```

We just created a new static pod named static-greenbox. Find it and delete it. (Important)

1. First, let's identify the node in which the pod called static-greenbox is created. To do this, run:
```bash
root@controlplane:~# kubectl get pods --all-namespaces -o wide  | grep static-greenbox
default       static-greenbox-node01                 1/1     Running   0          19s     10.244.1.2   node01       <none>           <none>
```

2. From the result of this command, we can see that the pod is running on node01.

3. Next, SSH to node01 and identify the path configured for static pods in this node.

**Important**: The path need not be /etc/kubernetes/manifests. Make sure to check the path configured in the kubelet configuration file.

```bash
root@controlplane:~# ssh node01 
root@node01:~# ps -ef |  grep /usr/bin/kubelet 
root        4147       1  0 14:05 ?        00:00:00 /usr/bin/kubelet --bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf --config=/var/lib/kubelet/config.yaml --container-runtime-endpoint=unix:///var/run/containerd/containerd.sock --pod-infra-container-image=registry.k8s.io/pause:3.9
root        4773    4733  0 14:05 pts/0    00:00:00 grep /usr/bin/kubelet
root@node01:~# grep -i staticpod /var/lib/kubelet/config.yaml
staticPodPath: /etc/just-to-mess-with-you
root@node01:~# 
```

4. Here the staticPodPath is /etc/just-to-mess-with-you

```bash
root@node01:/etc/just-to-mess-with-you# ls
greenbox.yaml
root@node01:/etc/just-to-mess-with-you# rm -rf greenbox.yaml 
root@controlplane:~# kubectl get pods --all-namespaces -o wide  | grep static-greenbox
root@controlplane:~# 
```
Question 1 | DNS / FQDN / Headless Service
 
Solve this question on: ssh cka6016

The Deployment controller in Namespace lima-control communicates with various cluster internal endpoints by using their DNS FQDN values.

Update the ConfigMap used by the Deployment with the correct FQDN values for:

- DNS_1: Service `kubernetes` in Namespace `default`
- DNS_2: Headless Service `department` in Namespace `lima-workload`
- DNS_3: Pod `section100` in Namespace `lima-workload`. It should work even if the Pod IP changes
- DNS_4: A Pod with IP 1.2.3.4 in Namespace kube-system

Ensure the Deployment works with the updated values.

Step 1 Edit config map

Step 2 Update dns names
```yaml
apiVersion: v1
data:
  DNS_1: kubernetes.default.svc.cluster.local                  # UPDATE
  DNS_2: department.lima-workload.svc.cluster.local            # UPDATE
  DNS_3: section100.section.lima-workload.svc.cluster.local    # UPDATE <POD>.<SVC>.<NAMESPACE>.svc.cluster.local
  DNS_4: 1-2-3-4.kube-system.pod.cluster.local                 # UPDATE
kind: ConfigMap
metadata:
  name: control-config
  namespace: lima-control
```

Question 2 | Create a Static Pod and Service
Solve this question on: `ssh cka2560`

Create a Static Pod named `my-static-pod` in Namespace `default` on the controlplane node. It should be of image `nginx:1-alpine` and have resource requests for `10m` CPU and `20Mi` memory.

Create a `NodePort` Service named `static-pod-service` which exposes that static Pod on port `80`.

```bash
cd /etc/kubernetes/manifests/
kubectl run my-static-pod --image=nginx:1-alpine -o yaml --dry-run=client > my-static-pod.yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: my-static-pod
  name: my-static-pod
spec:
  containers:
  - image: nginx:1-alpine
    name: my-static-pod
    ports:
      containerPort: 80
    resources:
      requests:
        cpu: 10m
        memory: 20Mi
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```
```bash
kubectl expose pod my-static-pod --name static-pod-service --port=80 --target-port=80 --type=nodePort --dry-run=client -o yaml
```

Question 3 | Kubelet client/server cert info
 
Solve this question on: `ssh cka5248`

Node `cka5248-node1` has been added to the cluster using `kubeadm` and TLS bootstrapping.

Find the `Issuer` and `Extended Key Usage` values on `cka5248-node1` for:

1. Kubelet Client Certificate, the one used for outgoing connections to the kube-apiserver
2. Kubelet Server Certificate, the one used for incoming connections from the kube-apiserver

Write the information into file `/opt/course/3/certificate-info.txt`.
```bash
ssh cka5248 
ssh cka5248-node1

ls  -l /var/lib/kubelet/pki

# For Client
openssl -x509 -text -noout -in  /var/lib/kubelet/pki/kubelet-client-current.pem
        # Issuer: CN = kubernetes
        #     X509v3 Extended Key Usage: 
        #         TLS Web Client Authentication

openssl -x509 -text -noout -in  /var/lib/kubelet/pki/kubelet.crt
        # Issuer: CN = cka5248-node1-ca@1730211854
        #     X509v3 Extended Key Usage: 
        #         TLS Web Server Authentication
```

```txt
# cka5248:/opt/course/3/certificate-info.txt
Issuer: CN = kubernetes
X509v3 Extended Key Usage: TLS Web Client Authentication
Issuer: CN = cka5248-node1-ca@1730211854
X509v3 Extended Key Usage: TLS Web Server Authentication
```

Question 4 | Pod Ready if Service is reachable


Solve this question on: ssh cka3200

Do the following in Namespace default:

1. Create a Pod named `ready-if-service-ready` of image `nginx:1-alpine`
2. Configure a `LivenessProbe` which simply executes command `true`
3. Configure a `ReadinessProbe` which does check if the url http://service-am-i-ready:80 is reachable, you can use `wget -T2 -O- http://service-am-i-ready:80` for this
4. Start the Pod and confirm it isn't ready because of the ReadinessProbe.

Then:

1. Create a second Pod named `am-i-ready` of image `nginx:1-alpine` with label `id: cross-server-ready`
2. The already existing Service `service-am-i-ready` should now have that second Pod as endpoint
3. Now the first Pod should be in ready state, check that

```bash
kubectl run ready-if-service-ready --image=nginx:1-alpine --dry-run=client -o yaml
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: ready-if-service-ready
  name: ready-if-service-ready
spec:
  containers:
  - image: nginx:1-alpine
    name: ready-if-service-ready
    resources: {}
    readinessProbe:
      exec:
        command:
        - "wget -T2 -O- http://service-am-i-ready:80"
    livenessProbe:
      exec:
        command:
        - "true"
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```

```bash
kubectl run ami-i-ready --image=nginx:1-alpine --dry-run=client -o yaml
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    id: cross-server-ready
  name: ami-i-ready
spec:
  containers:
  - image: nginx:1-alpine
    name: ami-i-ready
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```

Question 5 | Kubectl sorting
 

Solve this question on: ssh cka8448

Create two bash script files which use kubectl sorting to:

1. Write a command into `/opt/course/5/find_pods.sh` which lists all Pods in all Namespaces sorted by their AGE (`metadata.creationTimestamp`)
2. Write a command into `/opt/course/5/find_pods_uid.sh` which lists all Pods in all Namespaces sorted by field `metadata.uid`

```bash
kubectl get po -A --sort-by=metadata.creationTimestamp

kubectl get po -A --sort-by=metadata.uid
```

Question 6 | Fix Kubelet

Solve this question on: `ssh cka1024`

1. There seems to be an issue with the kubelet on controlplane node `cka1024`, it's not running.
2. Fix the kubelet and confirm that the node is available in Ready state.
3. Create a Pod called success in default Namespace of image nginx:1-alpine.

```bash
# Few things we do to troubleshoot
# Use below command to check status of kubelet. It will also show path of config and service file
systemctl status kubelet

# We can also check are we able to connect node
kubectl get node

# We can also check the kubelet command path
whereis kubelet

# We can check config as well
cat /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
```

Question 7 | Etcd Operations

Solve this question on: `ssh cka2560`

You have been tasked to perform the following etcd operations:

1. Run `etcd --version`n and store the output at `/opt/course/7/etcd-version`

2. Make a snapshot of etcd and save it at `/opt/course/7/etcd-snapshot.db`

```bash

kubectl -n kube-system exec etcd-cka2560 -- etcd --version > /opt/course/7/etcd-version


cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep etcd # Get following values
# - --etcd-cafile=/etc/kubernetes/pki/etcd/ca.crt
# - --etcd-certfile=/etc/kubernetes/pki/apiserver-etcd-client.crt
# - --etcd-keyfile=/etc/kubernetes/pki/apiserver-etcd-client.key
# - --etcd-servers=https://127.0.0.1:2379

# To Backup
ETCDCTL_API=3 etcdctl snapshot save /opt/course/7/etcd-snapshot.db \
--cacert /etc/kubernetes/pki/etcd/ca.crt \
--cert /etc/kubernetes/pki/etcd/server.crt \
--key /etc/kubernetes/pki/etcd/server.key

# To Restore
ETCDCTL_API=3 etcdctl snapshot restore /opt/course/7/etcd-snapshot.db \
--data-dir /var/lib/etcd-snapshot \
--cacert /etc/kubernetes/pki/etcd/ca.crt \
--cert /etc/kubernetes/pki/etcd/server.crt \
--key /etc/kubernetes/pki/etcd/server.key
```

Reference: [Operating etcd clusters for Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)

Question 8 | Get Controlplane Information

Solve this question on: ssh cka8448

Check how the controlplane components `kubelet`, `kube-apiserver`, `kube-scheduler`, `kube-conrtoller-manager` and `etcd` are started/installed on the controlplane node.

Also find out the name of the DNS application and how it's started/installed in the cluster.

Write your findings into file `/opt/course/8/controlplane-components.txt`. The file should be structured like:

```txt
kubelet: [TYPE]
kube-apiserver: [TYPE]
kube-scheduler: [TYPE]
kube-controller-manager: [TYPE]
etcd: [TYPE]
dns: [TYPE] [NAME]
```
Choices of `[TYPE]` are: `not-installed`, `process`, `static-pod`, `pod`

```txt
# /opt/course/8/controlplane-components.txt
kubelet: process
kube-apiserver: static-pod
kube-scheduler: static-pod
kube-controller-manager: static-pod
etcd: static-pod
dns: pod coredns
```

Question 9 | Kill Scheduler, Manual Scheduling
 

Solve this question on: `ssh cka5248`

Temporarily stop the `kube-scheduler`, this means in a way that you can start it again afterwards.

Create a single Pod named `manual-schedule` of image `httpd:2-alpine`, confirm it's created but not scheduled on any node.

Now you're the scheduler and have all its power, manually schedule that Pod on node `cka5248`. Make sure it's running.

Start the `kube-scheduler` again and confirm it's running correctly by creating a second Pod named `manual-schedule2` of image `httpd:2-alpine` and check if it's running on cka5248-node1.

```bash
kubectl run manual-schedule --image=httpd:2-alpine --dry-run=client -o yaml
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: manual-schedule
  name: manual-schedule
spec:
  nodeName: cka5248 # I add node manually
  containers:
  - image: httpd:2-alpine
    name: manual-schedule
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
---
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: manual-schedule2
  name: manual-schedule2
spec:
  containers:
  - image: httpd:2-alpine
    name: manual-schedule2
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```
```bash
cd /etc/kubernetes/manifests/
mv kube-scheduler.yaml ../ # Do it for  manual-schedule
mv kube-scheduler.yaml ./manifests # Do it for  manual-schedule2
```

Question 10 | PV PVC Dynamic Provisioning

Solve this question on: `ssh cka6016`


There is a backup Job which needs to be adjusted to use a PVC to store backups.

Create a `StorageClass` named `local-backup` which uses `provisioner: rancher.io/local-path` and `volumeBindingMode: WaitForFirstConsumer`. To prevent possible data loss the StorageClass should keep a PV retained even if a bound PVC is deleted.

Adjust the Job at `/opt/course/10/backup.yaml` to use a PVC which request `50Mi` storage and uses the new StorageClass.

Deploy your changes, verify the Job completed once and the PVC was bound to a newly created PV.

 
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-backup
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: rancher.io/local-path
reclaimPolicy: Retain # default value is Delete
allowVolumeExpansion: true
mountOptions:
  - discard # this might enable UNMAP / TRIM at the block storage layer
volumeBindingMode: WaitForFirstConsumer
parameters:
  guaranteedReadWriteLatency: "true" # provider-specific
```
Reference: [Storage](https://kubernetes.io/docs/concepts/storage/storage-classes/)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: task-pv-volume
  labels:
    type: local
spec:
  storageClassName: local-backup
  capacity:
    storage: 50Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/mnt/data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: task-pv-claim
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 50Mi
---
apiVersion: v1
kind: Pod
metadata:
  name: task-pv-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: task-pv-claim
  containers:
    - name: task-pv-container
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
        - mountPath: "/usr/share/nginx/html"
          name: task-pv-storage
```

Question 11 | Create Secret and mount into Pod

Create Namespace secret and implement the following in it:

Create Pod `secret-pod` with image `busybox:1`. It should be kept running by executing `sleep 1d` or something similar

Create the existing Secret `/opt/course/11/secret1.yaml` and mount it `readonly` into the Pod at `/tmp/secret1`

Create a new Secret called `secret2` which should contain `user=user1` and `pass=1234`. These entries should be available inside the Pod's container as environment variables `APP_USER` and `APP_PASS`

```bash
kubectl run secret-pod --image=busybox:1 --dry-run=client -o yaml --command -- sleep 1d 
kubectl create secret generic secret2 --from-literal=user=user1 --from-literal=pass=1234
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: secret-pod
  name: secret-pod
spec:
  volumes:
    - name: secret-volume
      secret:
        secretName: secret1
  containers:
  - command:
    - sleep
    - 1d
    image: busybox:1
    env:
    - name: APP_USER
      valueFrom:
        secretKeyRef:
          name: secret2
          key: user
    - name: APP_PASS
      valueFrom:
        secretKeyRef:
          name: secret2
          key: pass
    name: secret-pod
    resources: {}
    volumeMounts:
      - name: secret-volume
        readOnly: true
        mountPath: "/tmp/secret1"
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```

Question 12 | Schedule Pod on Controlplane Nodes
 

Solve this question on: ssh cka5248

Create a Pod of image `httpd:2-alpine` in Namespace default.

The Pod should be named `pod1` and the container should be named` pod1-container`.

This Pod should only be scheduled on controlplane nodes.

Do not add new labels to any nodes.


We can use `nodeaffinity` or `nodeSelector`
```bash
kubectl 
```

```yaml
```
Question 1 | Contexts:
- Solve this question on: `ssh cka9412`
- You're asked to extract the following information out of kubeconfig file `/opt/course/1/kubeconfig` on `cka9412`:
  - Write all kubeconfig context names into `/opt/course/1/contexts`, one per line
  - Write the name of the current context into `/opt/course/1/current-context`
  - Write the client-certificate of user `account-0027` base64-decoded into `/opt/course/1/cert`
```bash
kubectl --kubeconfig /opt/course/1/kubeconfig config get-contexts -oname
kubectl --kubeconfig /opt/course/1/kubeconfig config get-contexts -oname > /opt/course/1/contexts

kubectl --kubeconfig /opt/course/1/kubeconfig config current-context
kubectl --kubeconfig /opt/course/1/kubeconfig config current-context > /opt/course/1/current-context

kubectl config view -oyaml --raw
echo LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUZIakNDQXdhZ.. | base64 -d
```
Question 2 | MinIO Operator, CRD Config, Helm Install

Solve this question on: `ssh cka7968`

- Install the MinIO Operator using Helm in Namespace `minio`. Then configure and create the Tenant CRD:
  - Create Namespace `minio`
  - Install Helm chart `minio/operator` into the new Namespace. The Helm Release should be called `minio-operator`
  - Update the Tenant resource in `/opt/course/2/minio-tenant.yaml` to include `enableSFTP: true` under features
  - Create the Tenant resource from `/opt/course/2/minio-tenant.yaml`

```bash
kubectl create ns minio

helm repo list
helm search repo

helm upgrade --install minio-operator minio/operator -n minio

kubectl get crd
kubectl apply -f /opt/course/2/minio-tenant.yaml
kubectl get tenant
```

Question 3 | Scale down StatefulSet

Solve this question on: ssh cka3962
- There are two Pods named `o3db-*` in Namespace `project-h800`. The Project H800 management asked you to scale these down to one replica to save resources.
```bash
kubectl scale sts o3db --replicas=1 -n project-h800
```

Question 4 | Find Pods first to be terminated

Solve this question on: ssh cka2556
- Check all available Pods in the Namespace `project-c13` and find the names of those that would probably be terminated first if the nodes run out of resources (cpu or memory).
- Write the Pod names into `/opt/course/4/pods-terminated-first.txt`.

```bash
kubectl describe po -n project-c13 | grep -A1 -E 'Request|^Name'

# or

kubectl get pods -n project-c13 -o jsonpath='{range .items[*]}{.metadata.name}{" => "}{.status.qosClass}{"\n"}{end}'

# or

kubectl get po -n kube-system -o jsonpath='{range .items[*]}{.metadata.name}{" => "}{.spec.containers[0].resources}{"\n"}{end}'
```



```markdown
| QoS Class      | Definition                        | Termination Priority |
| -------------- | --------------------------------- | -------------------- |
| **BestEffort** | No resource requests/limits set   | **First**            |
| **Burstable**  | Some requests/limits set          | Medium               |
| **Guaranteed** | CPU and memory requests == limits | Last                 |
```

Question 5 | Kustomize configure HPA Autoscaler

Solve this question on: ssh cka5774
- Previously the application `api-gateway` used some external autoscaler which should now be replaced with a HorizontalPodAutoscaler (HPA). The application has been deployed to Namespaces `api-gateway-staging` and `api-gateway-prod` like this:

```bash
kubectl kustomize /opt/course/5/api-gateway/staging | kubectl apply -f -
kubectl kustomize /opt/course/5/api-gateway/prod | kubectl apply -f -
```
Using the Kustomize config at `/opt/course/5/api-gateway` do the following:

- Remove the ConfigMap horizontal-scaling-config completely
- Add HPA named api-gateway for the Deployment api-gateway with min 2 and max 4 replicas. It should scale at 50% average CPU utilisation
- In prod the HPA should have max 6 replicas
- Apply your changes for staging and prod so they're reflected in the cluster

```bash
# Step 1: Go to folder and check each env dry run
cd /opt/course/5/api-gateway
kubectl kustomize base
kubectl kustomize staging
kubectl kustomize prod

# Step 2: Remove the ConfigMap (horizontal-scaling-config) completely from base/ folder
rm horizontal-scaling-config.yaml

# Step 3: Add HPA named api-gateway for the Deployment api-gateway with min 2 and max 4 replicas. It should scale at 50% average CPU utilisation
kubectl autoscale deploy api-gateway --min=2 --max=4 --cpu-percent=50 --dry-run=client -o yaml


# Ste 4: In prod the HPA should have max 6 replicas
vim /opt/course/5/api-gateway/overlays/prod/kustomization.yaml

## update line

```

```yaml
patches:
  - patch: |
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: myapp
      spec:
        replicas: 1
  - patch: |
      apiVersion: autoscaling/v1
      kind: HorizontalPodAutoscaler
      metadata:
        name: myapp
      spec:
        maxReplicas: 6
        minReplicas: 2
        scaleTargetRef:
          apiVersion: apps/v1
          kind: Deployment
          name: myapp
        targetCPUUtilizationPercentage: 50
      status:
        currentReplicas: 0
        desiredReplicas: 0
```

Question 6 | Storage, PV, PVC, Pod volume

Solve this question on: ssh cka7968

- Create a new `PersistentVolume` named `safari-pv`. It should have a capacity of `2Gi`, `accessMode` `ReadWriteOnce`, `hostPath` `/Volumes/Data` and no `storageClassName` defined.

- Next create a new `PersistentVolumeClaim` in Namespace `project-t230` named `safari-pvc` . It should request `2Gi` storage, accessMode `ReadWriteOnce` and should not define a `storageClassName`. The PVC should bound to the PV correctly.

- Finally create a new Deployment `safari` in Namespace `project-t230` which mounts that volume at `/tmp/safari-data`. The Pods of that Deployment should be of image `httpd:2-alpine`

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: safari-pv
  labels:
    type: local
spec:
  storageClassName: ""
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/Volumes/Data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: safari-pvc
  namespace: project-t230
spec:
  storageClassName: ""
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 2Gi
---
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: safari
  name: safari
  namespace: project-t230
spec:
  replicas: 1
  selector:
    matchLabels:
      app: safari
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: safari
    spec:
      containers:
      - image: httpd:2-alpine
        name: httpd
        resources: {}
        volumeMounts:
          - mountPath: "/tmp/safari-data"
            name: task-pv-storage
    volumes:
      - name: task-pv-storage
        persistentVolumeClaim:
          claimName: safari-pvc
```

Reference: [Configure a Pod to Use a PersistentVolume for Storage](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/)


Question 7 | Node and Pod Resource Usage

Solve this question on: ssh cka5774

The metrics-server has been installed in the cluster. Write two bash scripts which use kubectl:
1. Script /opt/course/7/node.sh should show resource usage of nodes

```bash
kubectl top node
```
2. Script /opt/course/7/pod.sh should show resource usage of Pods and their containers

```bash
kubectl top po --containers=true
```

Question 8 | Update Kubernetes Version and join cluster

Solve this question on: ssh cka3962

Your coworker notified you that node cka3962-node1 is running an older Kubernetes version and is not even part of the cluster yet.

1. Update the node's Kubernetes to the exact version of the controlplane
2. Add the node to the cluster using kubeadm

```bash
# Step 1: ssh to controlplane node
ssh cka3962

k get node # It will show VERSION ex: v1.33.1

# Step 2: ssh to worker node
ssh cka3962-node1

# Step 3: Become root
sudo -i

# Check version of kubectl, kubelet and kubeadm
kubectl version
kubelet --version
kubeadm version

# Step 4: Install kubectl, kubelet and kubeadm
apt update
apt install kubectl=1.33.1-1.1 kubelet=1.33.1-1.1 kubeadm=1.33.1-1.1

# Step 5: Restart kubelet
service kubelet restart
service kubelet status

# Step 6: Add node to cluster
ssh cka3962 # master node
sudo -i
kubeadm token create --print-join-command # kubeadm join 192.168.100.31:6443 --token u1n13d.x68l08ofgamv754u --discovery-token-ca-cert-hash sha256:8945ece6fdf32ae6ee85483acd7ade2e1ce878615bc8972cd5e86031e3d99325 
kubeadm token list

ssh cka3962-node1 # worker node
kubeadm join 192.168.100.31:6443 --token u1n13d.x68l08ofgamv754u --discovery-token-ca-cert-hash sha256:8945ece6fdf32ae6ee85483acd7ade2e1ce878615bc8972cd5e86031e3d99325 
service kubelet status

kubectl get node # It should show worker node with Ready status
```

Question 9 | Contact K8s Api from inside Pod

Solve this question on: ssh cka9412

There is ServiceAccount `secret-reader` in Namespace `project-swan`. Create a Pod of image `nginx:1-alpine` named `api-contact` which uses this ServiceAccount.

Exec into the Pod and use curl to manually query all Secrets from the Kubernetes Api.

Write the result into file `/opt/course/9/result.json`.

- Helper env setup

```bash
kubectl create ns project-swan

# Creating service account
kubectl create serviceaccount secret-reader -n project-swan
```

```bash
# Creating role for service account
kubectl create clusterrole secret-reader-role --verb=get,list,watch --resource=secrets
```

```bash
# Creating role  binding for service account and role
kubectl create clusterrolebinding secret-reader-binding \
  --clusterrole=secret-reader-role \
  --serviceaccount=project-swan:secret-reader
```

- Step 1: Create a pod using adhoc command
```bash
kubectl run  api-contact --image=nginx:1-alpine -n project-swan --dry-run=client -o yaml
```
```yaml
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: api-contact
  name: api-contact
  namespace: project-swan
spec:
  serviceAccountName: secret-reader # added manually 
  containers:
  - image: nginx:1-alpine
    name: api-contact
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```
- Step 2: Apply changes
```bash
kubectl apply -f api-contact.yaml
```
- Step 3: Check now new is able to get secrets
```bash
kubectl auth can-i get secret --as system:serviceaccount:project-swan:secret-reader
```

- Step 4: Go inside the pod
```bash
kubectl exec -it api-contact -n project-swan -- bash
```
- Step 5: Use Token to authenticate
```bash
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
curl --cacert ${CACERT} https://kubernetes.default/api/v1/secrets -H "Authorization: Bearer ${TOKEN}"
```

- Step 6: Write down all secrets in `/opt/course/9/result.json`

Reference: [configure-service-account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)


Question 10 | RBAC ServiceAccount Role RoleBinding

Solve this question on: ssh cka3962

Create a new ServiceAccount `processor` in Namespace `project-hamster`. Create a `Role` and `RoleBinding`, both named `processor` as well. These should allow the new SA to only create `Secrets` and `ConfigMaps` in that Namespace.

```bash
kubectl create sa processor -n project-hamster

kubectl create role processor  --verb=create --resource=secrets --resource=configmap -n project-hamster

kubectl create role-binding --role=processor --serviceaccount=processor -n project-hamster
```

Question 11 | DaemonSet on all Nodes

Solve this question on: ssh cka2556


Use Namespace `project-tiger` for the following. Create a DaemonSet named `ds-important` with `image httpd:2-alpine` and labels `id=ds-important` and `uuid=18426a0b-5f59-4e10-923f-c0e078e82462`. The Pods it creates should request `10 millicore` cpu and `10 mebibyte memory`. The Pods of that DaemonSet should run on all nodes, also controlplanes.

```bash
kubectl create deployment ds-important --image=httpd:2-alpine -n project-tiger --dry-run=client -o yaml
```
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  creationTimestamp: null
  labels:
    app: ds-important
  name: ds-important
  namespace: project-tiger
spec:
  # replicas: 1 # remove this
  selector:
    matchLabels:
      app: ds-important
  # strategy: {} # remove this
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: ds-important
    spec:
      containers:
      - image: httpd:2-alpine
        name: httpd
        resources:
          limits:
            cpu: 10m
            memory: 10Mi
          requests:
            cpu: 10m
            memory: 10Mi        
status: {}
```
Reference: [Daemonset](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)


Question 12 | Deployment on all Nodes

Solve this question on: ssh cka2556

Implement the following in Namespace project-tiger:

- Create a Deployment named `deploy-important` with `3` replicas
- The Deployment and its Pods should have label `id=very-important`
- First container named `container1` with image `nginx:1-alpine`
- Second container named `container2` with image `google/pause`
- There should only ever be one Pod of that Deployment running on one worker node, use topologyKey: `kubernetes.io/hostname` for this

Note: There are two possible ways, one using `podAntiAffinity` and one using `topologySpreadConstraint`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: deploy-important
    id: very-important
  name: deploy-important
spec:
  replicas: 3
  selector:
    matchLabels:
      app: deploy-important
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: deploy-important
    spec:
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: kubernetes.io/hostname
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            id: very-important
      containers:
      - image: nginx:1-alpine
        name: container1
        resources: {}
      - image: google/pause
        name: container2
        resources: {}
```

Reference: [Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)


Question 13 | Gateway Api Ingress

Solve this question on: ssh cka7968

The team from Project r500 wants to replace their `Ingress` (networking.k8s.io) with a `Gateway Api` (gateway.networking.k8s.io) solution. The old Ingress is available at `/opt/course/13/ingress.yaml`.

Perform the following in Namespace `project-r500` and for the already existing Gateway:
1. Create a new `HTTPRoute` named `traffic-director` which replicates the routes from the old Ingress
2. Extend the new `HTTPRoute` with path `/auto` which redirects to mobile if the User-Agent is exactly mobile and to desktop otherwise

The existing Gateway is reachable at `http://r500.gateway:30080` which means your implementation should work for these commands:

```bash
curl r500.gateway:30080/desktop
curl r500.gateway:30080/mobile
curl r500.gateway:30080/auto -H "User-Agent: mobile" 
curl r500.gateway:30080/auto
```
- Helper env setup
```bash
kubectl create ns project-r500
```

```yaml
# cka7968:/opt/course/13/ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: traffic-director
spec:
  ingressClassName: nginx
  rules:
    - host: r500.gateway
      http:
        paths:
          - backend:
              service:
                name: web-desktop
                port:
                  number: 80
            path: /desktop
            pathType: Prefix
          - backend:
              service:
                name: web-mobile
                port:
                  number: 80
            path: /mobile
            pathType: Prefix
```

1. Solution of Point 1
- Step 1: Check current setup
```bash
kubectl get gateway -A # It will show gateway name
kubectl get gatewayclass -A

curl r500.gateway:30080 # Do check it is reachable

vim /opt/course/13/ingress.yaml # refer this ingress 
```
- Step 2: Create new HTTPRoute
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: traffic-director
spec:
  parentRefs:
  - name: main          # existing Gateway name
  hostnames:
  - "r500.gateway"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /desktop
    backendRefs:
    - name: web-desktop
      port: 80

  - matches:
    - path:
        type: PathPrefix
        value: /web-mobile
    backendRefs:
    - name: web-mobile
      port: 80
```

- Step 3: Check HTTPRoute
```bash
kubectl get httproute -n project-r500
```
```bash
NAME               HOSTNAMES       AGE
traffic-director   ["r500.gateway"]   7s
```

2. Solution of Point 2
```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: traffic-director
spec:
  parentRefs:
  - name: main          # existing Gateway name
  hostnames:
  - "r500.gateway"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /desktop
    backendRefs:
    - name: web-desktop
      port: 80

  - matches:
    - path:
        type: PathPrefix
        value: /web-mobile
    backendRefs:
    - name: web-mobile
      port: 80

  - matches:
    - path:
        type: PathPrefix
        value: /auto
      headers:
      - name: user-agent
        type: Exact
        value: mobile
    backendRefs:
    - name: web-mobile
      port: 80

  - matches:
    - path:
        type: PathPrefix
        value: /auto
      headers:
      - name: user-agent
        type: Exact
        value: desktop
    backendRefs:
    - name: web-desktop
      port: 80
```
Reference: [Gateway](https://kubernetes.io/docs/concepts/services-networking/gateway/)


Question 14 | Check how long certificates are valid

Solve this question on: ssh cka9412

 

Perform some tasks on cluster certificates:

1. Check how long the kube-apiserver server certificate is valid using `openssl` or `cfssl`. Write the expiration date into `/opt/course/14/expiration`. Run the kubeadm command to list the expiration dates and confirm both methods show the same one
2. Write the kubeadm command that would renew the kube-apiserver certificate into `/opt/course/14/kubeadm-renew-certs.sh`

1. How long the kube-apiserver server certificate is valid using `openssl`
```bash
# To check validity of certificate
openssl x509 -noout -text -in /etc/kubernetes/pki/apiserver.crt 
```

```bash
# To check expiration
kubeadm certs check-expiration
apiserver                  Oct 29, 2025 14:19 UTC   356d    ca         no      
apiserver-etcd-client      Oct 29, 2025 14:19 UTC   356d    etcd-ca    no      
apiserver-kubelet-client   Oct 29, 2025 14:19 UTC   356d    ca         no 
.
.
.
```


2. kubeadm command that would renew the kube-apiserver certificate
```bash
# cka9412:/opt/course/14/kubeadm-renew-certs.sh
kubeadm certs renew apiserver
```

Question 15 | NetworkPolicy

Solve this question on: ssh cka7968

There was a security incident where an intruder was able to access the whole cluster from a single hacked backend Pod.

To prevent this create a NetworkPolicy called `np-backend` in Namespace `project-snake`. It should allow the `backend-*` Pods only to:
- Connect to `db1-*` Pods on port `1111`
- Connect to `db2-*` Pods on port `2222`
Use the app Pod labels in your policy.


```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: np-backend
  namespace: project-snake
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Egress
  egress:
  - to:
    - podSelector:
        matchExpressions:
        - app: db1
    ports:
    - protocol: TCP
      port: 1111
  - to:
    - podSelector:
        matchExpressions:
        - app: db2
    ports:
    - protocol: TCP
      port: 2222
```
Reference: [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

Question 16 | Update CoreDNS Configuration

- Step 1: Get config map
```bash 
kubectl get cm coredns -n kube-system -o yaml > coredns.yaml
```
- Step 2: Apply Changes
```yaml
apiVersion: v1
data:
  Corefile: |
    .:53 {
        errors
        health {
           lameduck 5s
        }
        ready
        kubernetes custom-domain cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
        }
        prometheus :9153
        forward . /etc/resolv.conf {
           max_concurrent 1000
        }
        cache 30
        loop
        reload
        loadbalance
    }
kind: ConfigMap
metadata:
  creationTimestamp: "2025-10-22T00:37:07Z"
  name: coredns
  namespace: kube-system
```

Question 17 | Find Container of Pod and check info

Solve this question on: ssh cka2556

In Namespace project-tiger create a Pod named `tigers-reunite` of image `httpd:2-alpine` with labels `pod=container` and `container=pod`. Find out on which node the Pod is scheduled. Ssh into that node and find the containerd container belonging to that Pod.

Using command crictl:

1. Write the `ID` of the container and the `info.runtimeType` into `/opt/course/17/pod-container.txt`
2. Write the logs of the container into `/opt/course/17/pod-container.log`

```bash
k -n project-tiger run tigers-reunite --image=httpd:2-alpine --labels "pod=container,container=pod"
k -n project-tiger get pod -o wide
```
1. 
```bash
ssh cka2556-node1
crictl ps | grep tigers-reunite
crictl inspect ba62e5d465ff0 | grep runtimeType
```

2. 
```bash
crictl logs ba62e5d465ff0
```
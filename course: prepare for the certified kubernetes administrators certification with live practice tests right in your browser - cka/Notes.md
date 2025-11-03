# Index
### Core Concept
1. Practice Tests - Pods                                                                 DONE
2. Practice Tests - Replicasets                                                          DONE
3. Practice Tests - Deployments                                                          DONE
4. Practice Tests - Namespaces                                                           DONE
5. Practice Tests - Services                                                             DONE
6. Practice Tests - Imperative Commands (kubectl create/delete/top/run )                 DONE

### Scheduling
7. Practice Tests - Manual Scheduling                                                    DONE
8. Practice Tests - Labels and Selectors                                                 DONE
9. Practice Tests - Taints and Toleration                                                DONE
10. Practice Tests - Node Affinity                                                       DONE
11. Practice Tests - Resource Limits                                                     DONE
12. Practice Tests - Daemonsets                                                          DONE
13. Practice Tests - Static Pods                                                         DONE
14. Practice Tests - Priority Classes                                                    DONE
15. Practice Tests - Multiple Schedulars                                                 DONE
16. Practice Tests - Admission Controller                                                DONE
17. Practice Tests - Validating and Mutating Admission Controller                        DONE

### Logging and Monitoring
18. Practice Test - Monitor Cluster Components                                           DONE
19. Practice Test - Managing Application Logs                                            DONE

### Application Life Cycle Management
20. Practice Test - Rolling Updates and Rollbacks                                        DONE
21. Practice Test - Commands and Arguments                                               DONE
22. Practice Test - Env Variables                                                        DONE
23. Practice Test - Secrets                                                              DONE
24. Practice Test - Multi Container PODs                                                 DONE
25. Practice Test - Init Containers                                                      DONE
26. Practice Test - Manual Scaling                                                       DONE
27. Practice Test - HPA                                                                  DONE
28. Practice Test - Install VPA                                                          DONE
29. Practice Test - Modifying CPU resources in VPA                                       DONE

### Cluster Maintenance
30. Practice Test - OS Upgrades                                                          DONE
31. Practice Test - Cluster Upgrade Process                                              DONE
32. Practice Test - Backup and Restore Methods                                           DONE

### Security
33. Practice Test - View Certificate Details                                             DONE
34. Practice Test - Certificates API                                                     DONE
35. Practice Test - KubeConfig                                                           DONE
36. Practice Test - Role Based Access Controls                                           DONE
37. Practice Test - Cluster Roles                                                        DONE
38. Practice Test - Service Accounts                                                     DONE
39. Practice Test - Image Security                                                       DONE
40. Practice Test - Security Contexts                                                    DONE
41. Practice Test - Network Policies                                                     DONE
42. Practice Test - Custom Resource Definition                                           DONE

### Storage
43. Practice Test - Persistent Volume Claims                                             DONE
44. Practice Test - Storage Class                                                        DONE

### Network
45. Practice Test - Explore Environment                                                  DONE
46. Practice Test - CNI                                                                  DONE
47. Practice Test - Networking CNIs                                                      DONE
48. Practice Test - Service Networking                                                   DONE
49. Practice Test - CoreDNS in Kubernetes                                                DONE
50. Practice Test - CKA - Ingress Networking - 1                                         DONE
51. Practice Test - CKA - Ingress Networking - 2                                         DONE
52. Practice Test - Gateway API                                                          DONE

### Install kubernetes "the kubeadm way"
53. Practice Tests - Cluster installation using kubeadm                                  DONE


# Architecture and their configuration
- controlplane
  - etcd
    - config PATH:
    - log PATH:
  - coreDNS
    - config PATH:
    - log PATH:  
  - kubelet
    - config PATH:
    - log PATH: 
  - kube-apiserver
    - config PATH:
    - log PATH: 
  - kube-proxy
    - Ways kube proxy manage service ip's
      - iptables
      - userspace
      - ipvs
    - config PATH:
    - log PATH: 
  - kube-schedular
    - config PATH:
    - log PATH: 
  - kube controller
    - config PATH:
    - log PATH: 
- worker node
  - kubelet
    - config PATH:
    - log PATH:
  - 
### Ad Hoc Commands

- kubectl create
  - Available Commands:

    - clusterrole: Create a cluster role
      - Create a cluster role named "pod-reader" that allows user to perform "get", "watch" and "list" on pods: `kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods`
      - Create a cluster role named "pod-reader" with ResourceName specified: `kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod`
      - Create a cluster role named "foo" with API Group specified: `kubectl create clusterrole foo --verb=get,list,watch --resource=rs.apps`
      - Create a cluster role named "foo" with SubResource specified: `kubectl create clusterrole foo --verb=get,list,watch --resource=pods,pods/status`
      - Create a cluster role name "foo" with NonResourceURL specified: `kubectl create clusterrole "foo" --verb=get --non-resource-url=/logs/*`
      - Create a cluster role name "monitoring" with AggregationRule specified: `kubectl create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"`

    - clusterrolebinding    Create a cluster role binding for a particular cluster role
      - Create a cluster role binding for user1, user2, and group1 using the cluster-admin cluster role: `kubectl create clusterrolebinding cluster-admin --clusterrole=cluster-admin --user=user1 --user=user2 --group=group1`

    - configmap             Create a config map from a local file, directory or literal value
      - Create a new config map named my-config based on folder bar: `kubectl create configmap my-config --from-file=path/to/bar`
      - Create a new config map named my-config with specified keys instead of file basenames on disk: `kubectl create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt`
      - Create a new config map named my-config with key1=config1 and key2=config2: `kubectl create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2`
      - Create a new config map named my-config from the key=value pairs in the file: `kubectl create configmap my-config --from-file=path/to/bar`
      - Create a new config map named my-config from an env file: `kubectl create configmap my-config --from-env-file=path/to/foo.env --from-env-file=path/to/bar.env`

    - cronjob               Create a cron job with the specified name
      - Create a cron job: `kubectl create cronjob my-job --image=busybox --schedule="*/1 * * * *"`
      - Create a cron job with a command: `kubectl create cronjob my-job --image=busybox --schedule="*/1 * * * *" -- date`

    - deployment            Create a deployment with the specified name
      - `kubectl create deploy testing --image=nginx` 
      - `kubectl create deployment testing --image=nginx -- sleep 1000`
      - `kubectl create deployment testing --image=nginx --replicas=3`
      - `kubectl create deployment testing --image=nginx --port=80`
      - `kubectl create deployment testing --image=busybox:latest --image=ubuntu:latest --image=nginx`

    - ingress Create an ingress with the specified name
      - Create a single ingress called 'simple' that directs requests to foo.com/bar to svc: `kubectl create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"`
      - Create a catch all ingress of "/path" pointing to service svc:port and Ingress Class as "otheringress": `kubectl create ingress catch-all --class=otheringress --rule="/path=svc:port"`
      - Create an ingress with two annotations: ingress.annotation1 and ingress.annotations2: `kubectl create ingress annotated --class=default --rule="foo.com/bar=svc:port" --annotation ingress.annotation1=foo --annotation ingress.annotation2=bla`
      - Create an ingress with the same host and multiple paths: `kubectl create ingress multipath --class=default --rule="foo.com/=svc:port" --rule="foo.com/admin/=svcadmin:portadmin"`
      - Create an ingress with multiple hosts and the pathType as Prefix: `kubectl create ingress ingress1 --class=default --rule="foo.com/path*=svc:8080" --rule="bar.com/admin*=svc2:http"`
      - Create an ingress with TLS enabled using the default ingress certificate and different path type: `kubectl create ingress ingtls --class=default --rule="foo.com/=svc:https,tls" --rule="foo.com/path/subpath*=othersvc:8080"`
      - Create an ingress with TLS enabled using a specific secret and pathType as Prefix: `kubectl create ingress ingsecret --class=default --rule="foo.com/*=svc:8080,tls=secret1"`
      - Create an ingress with a default backend: `kubectl create ingress ingdefault --class=default --default-backend=defaultsvc:http --rule="foo.com/*=svc:8080,tls=secret1"`
    - job                   Create a job with the specified name
      - Create a job: `kubectl create job my-job --image=busybox`
      - Create a job with a command: `kubectl create job my-job --image=busybox -- date`
      - Create a job from a cron job named "a-cronjob": `kubectl create job test-job --from=cronjob/a-cronjob`

    - namespace             Create a namespace with the specified name
      - `kubectl create ns testing`

    - poddisruptionbudget   Create a pod disruption budget with the specified name

    - priorityclass         Create a priority class with the specified name
      - Create a priority class named high-priority: `kubectl create priorityclass testing --value=100000 --description="High priority" --global-default=false`
      - Create a priority class named default-priority that is considered as the global default priority: `kubectl create priorityclass default-priority --value=1000 --global-default=true --description="default priority"`
      - Create a priority class named high-priority that cannot preempt pods with lower priority: `kubectl create priorityclass high-priority --value=1000 --description="high priority" --preemption-policy="Never"`

    - quota                 Create a quota with the specified name

    - role                  Create a role with single rule

    - rolebinding           Create a role binding for a particular role or cluster role

    - secret                Create a secret using a specified subcommand
      - `kubectl create secret docker-registry testing --docker-server=<your-registry-server> --docker-username=<your-username> --docker-password=<your-password> --docker-email=<your-email>`

    - service               Create a service using a specified subcommand
      - Available Commands:
        - clusterip      Create a ClusterIP service
          - Create a new ClusterIP service named my-cs: `kubectl create svc clusterip my-cs --tcp=5678:8080`
          - Create a new ClusterIP service named my-cs (in headless mode): `kubectl create svc clusterip my-cs --clusterip="None"`

        - externalname   Create an ExternalName service
        - loadbalancer   Create a LoadBalancer service
        - nodeport       Create a NodePort service

    - serviceaccount        Create a service account with the specified name

    - token                 Request a service account token

- kubectl expose
  - Create a service for a replicated `nginx`, which serves on port `80` and connects to the containers on port `8000`: `kubectl expose rc nginx --port=80 --target-port=8000`
  - Create a service for a `replication controller` identified by type and name specified in "nginx-controller.yaml": `kubectl expose -f nginx-controller.yaml --port=80 --target-port=8000`
  - Create a service for a pod `valid-pod`, which serves on port `444` with the name "`frontend`": `kubectl expose pod valid-pod --port=444  --name=frontend`\
  - Create a second service based on the above service, exposing the container port `8443` as port `443` with the name "nginx-https": `kubectl expose service nginx --port=443 --target-port=8443 --name=nginx-https`
  - Create a service for a replicated nginx using replica set, which serves on port 80 and connects to the containers on port 8000: `kubectl expose rs nginx --port=80 --target-port=8000`
  - Create a service for an `nginx` deployment, which serves on port `80` and connects to the containers on port `8000`: `kubectl expose deploy nginx --port=80 --target-port=8000`

- kubectl run
  - `kubectl run nginx --image=nginx`
- kubectl set
- kubectl explain
  - `kubectl explain storageclass --recursive`
  - `kubectl explain netpol --recursive`
- kubectl get
  - `kubectl get po`
- kubectl edit
  - `kubectl edit -it podName/deployName/statefulSet`
- kubectl delete
  - `kubectl delete deploy deployName`
- kubectl rollout
  - Available Commands:
    - history       View rollout history
    - pause         Mark the provided resource as paused
    - restart       Restart a resource
      - Restart a deployment: `kubectl rollout restart deploy/abc`
      - Restart deployments with the 'app=nginx' label: `kubectl rollout restart deploy --selector=app=nginx`
    - resume        Resume a paused resource
    - status        Show the status of the rollout
      - Check the rollout status of a daemonset: `kubectl rollout status daemonset/foo`
    - undo          Undo a previous rollout
      - Rollback to the previous deployment: `kubectl rollout undo deployment/abc`


- kubectl scale
  - `kubectl scale deploy testing --replicas=3`
- kubectl autoscale
  - `kubectl autoscale deployment testing  --min=2 --max=10 --cpu-percent=80 -o yaml --dry-run=client`
  - `kubectl autoscale rc testing  --min=2 --max=10 --cpu-percent=80 -o yaml --dry-run=client`
- kubectl certificate
- kubectl cluster-info
  - `kubectl cluster-info`
- kubectl top
  - `kubectl top po`
- kubectl cordon
  - `kubectl cordon NODE01`
- kubectl uncordon
  - `kubectl uncordon NODE01`
- kubectl drain
  - `kubectl drain NODE01`
- kubectl taint
  - `kubectl taint nodes NODE01 dedicated=special-user:NoSchedule`
  - `kubectl taint nodes NODE01 dedicated-`
  - `kubectl taint nodes NODE01 bar:NoSchedule`

- kubectl api-resources
- kubectl config
  - `kubectl config get-contexts` // list all context
  - `kubectl config get-contexts -o name` // list all context
  - `kubectl config current-context` // current contect
  - `kubectl config use-context cluster2` // to switch from one cluster to another
  - `kubectl --kube-config /opt/course/1/kubeconfig `


- helm 
  - `helm search repo <keyword>` # To Search for specific repo
  - `helm repo list` # List down every repo
  - `helm install minio ` # Install minio
  - `helm install my-nginx bitnami/nginx` # Install nginx
  - `helm repo add bitnami https://charts.bitnami.com/bitnami` # Add repo
  - `helm search repo`
  - `helm pull ingress-nginx/ingress-nginx --untar` # Download repo locally
  - `helm template ingress-nginx ingress-nginx/ingress-nginx --values ingress-nginx/values.yaml` # Check output template before applying
  - `helm show values ingress-nginx/ingress-nginx` # Show values

- kustomize
  - `kubectl kustomiz <DIR>`
  - `kubectl apply -k <DIR>`
  - `kubectl delete -k <DIR>`


- What is `--aggregation-rule`
  - Used when creating a ClusterRole that is automatically built (aggregated) from other ClusterRoles.
  - Instead of manually listing verbs/resources, you add a label selector.
  - Any ClusterRole that matches this selector will have its rules merged into your role.

- What is `--non-resource-url`
  - Grants permissions to access API endpoints that are not tied to resources.
  - These are endpoints like /healthz, /metrics, /logs/*, etc.
  - Useful when you want to give monitoring or debugging access without touching resources.
- What is `--default-backend`
- List down all the service deployed as service in node `systemctl list-units --type=service | grep kube`
- Decode Certificate: `openssl x509 -in <PATH> -text -noout`

### Deployment Strategy in kubernetes
  - Rolling Update
  - Recreate


# Util

- `kubectl auth can-i create secrets --as=system:serviceaccount:project-hamster:processor -n project-hamster`
- `kubeadm token create --print-join-command`
- `kubectl version`
- `kubeadm version`


# Commands
- `ip route show`: shows routes and gateway
- `openssl x509 -in /etc/kubernetes/pki/apiserver.crt  -text -noout`: decode certificate
- `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -enddate`: check end date
- `ip link`:
- `ip addr`: 
- `ip addr add`:
- `route & ip route`: To see route tables
- `ip route add`: Add routes in linux
- `nslookup <dns name>`
- `dig`
- `netstat -tulnp | grep kube-scheduler`: Check which port kube schedular is listening
- `netstat -tulnp | grep kube`
- Vim Command
  - `syntax on`
  - `set number`
  - `1,10d`

# Networking
- Switch: 
  - HELPS TO CONNECT TWO SERVERS
- ROUTER: 
  - HELPS TO CONNECT TWO DIFF NETWORK
  - ROUTERS HAS 2 or more IPs 
- GATEWAY:
- IP FORWARD
  - File: /proc/sys/net/ipv4/ip_forward
    - Default is 0:
  - File: /etc/sysctl.conf
    - net.ipv4.ip_forward=0 //Default
- DNS: To manage all hosts ip's
  - `/etc/resolv.conf`: 
    - nameserver <ip>
    - search mycompany.com
  - `/etc/nsswitch.conf`: hosts: files(`/etc/hosts`) dns
- Records Types
- Network Namespaces
  - To create network namespace: `ip netns add red` or `ip netns add blue`
  - To list: `ip netns`
  - To list: `ip link`
  - To list inside the namespace: `ip netns exec red ip link` or `ip -n red link`
  - To see arp table: `arp`
  - To connect two network interfaces: 
    - `ip link veth-red type veth peer name veth-blue`
    - `ip link set veth-red netns red` // attach with red interface
    - `ip link set veth-blue netns blue` // attach with blue interface
    - `ip -n red addr add 192.168.15.1 dev veth-red` // give ip 
    - `ip -n blue addr add 192.168.15.2 dev veth-blue` // give ip 
    - `ip -n red link set veth-red up` 
    - `ip -n blue link set veth-blue up`
    - Try to ping from red to blue: `ip netns exec red ping 192.168.15.2`
    - Try to arp table: `ip netns exec red arp` // red is now able to identify blue and it is same for blue as well
    - To delete link pair b/w red and blue: `ip -n red link del veth-red`
  - Virtual Switch
    - Linux Bridge & Open vSwitch
    - Establish connectivity in between network interfaces and external system
      - System A[Network namespace (v-net-0) -> eth0 (Ethernet)] -> Sytem B(External System)
      - We need to update route
      - We need to update NAT iptable
  - Docker Networks
    - None: `docker run --network=none nginx`
    - Host: `docker run --network=host nginx`
    - Bridge:
  - Container Network Interface (CNI)
    - cni config PATH: 
      - `/etc/cni/net.d`
      - `/opt/cni/bin`
    - weave works (cni plugin tool)


# Improvement Required

- Services and Networking
  - Network Policy
  - Ingress & Egress
  - CoreDNS
  - Networking CNI
  - Gateway CNI

- Cluster Architecture, Installation and Configuration
  - Installation of each services
  - Log Path Of Each Services
  - Backup and restore

- Helm
- Kustomize
- Crictl
- Containerd
- Docker

- Troubleshooting
  - jsonpath=[]

# Reference

- [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Persistent Volume & Persistent Volume Claim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Troubleshooting Clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [CoreDNS](https://kubernetes.io/docs/tasks/administer-cluster/coredns/)
- [Ports and Protocols](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
- [2025 CKA Exam Questions & Solutions UPDATE! | Full Walkthrough!](https://www.youtube.com/watch?v=eGv6iPWQKyo)
- [CKAD/CKA Exam Hack: Navigating the Docs Like a Pro](https://www.youtube.com/watch?v=ffejoGo-rnE)
- [Kubernetes CoreDNS](https://coredns.io/plugins/kubernetes/)
- [Kubernetes DNS-Based Service Discovery](https://github.com/kubernetes/dns/blob/master/docs/specification.md)
- [Installing Addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/)
- [Cluster Networking](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-network-model)

# PREVIOUSLY ASKED QUESTIONS

- Manual Scaling                                -> DONE
- HELM TEMPLATE ARGO CD & HELM VALUES           -> DONE
- NETWORK POLICY                                -> DONE
- COREDNS                                       -> DONE
- PVC AND PV WITH HOST PATH                     -> DONE
- SIDE CAR                                      -> DONE
- DAEMONSET                                     -> DONE
- PRIORITY CLASSES                              -> DONE
- HPA                                           -> DONE
- CLUSTER TROUBLESHOOTING                       -> DONE
- WORKER NODE IS DOWN TRY TO FIGURE OUT WHY     -> DONE
- CLUSTER ROLE AND ROLEBINDING                  -> DONE
- CREATE DEPLOYMENTS AND SERVICES               -> DONE
- NAMESPACE                                     -> DONE
- INGRESS CONTROLLER TO GATEWAY CNI             -> DONE
- INIT CONTAINER                                -> DONE
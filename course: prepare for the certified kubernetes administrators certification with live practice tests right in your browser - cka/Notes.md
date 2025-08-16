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
8. Practice Tests - Labels and Selectors
9. Practice Tests - Taints and Toleration
10. Practice Tests - Node Affinity
11. Practice Tests - Resource Limits                                                     DONE
12. Practice Tests - Daemonsets
12. Practice Tests - Static Pods                                                         DONE
13. Practice Tests - Priority Classes


### Install kubernetes "the kubeadm way"
Practice Tests - Cluster installation using kubeadm


# Important commands

- Imperative Commands
    - kubectl run nginx --image=nginx
    - kubectl delete
    - kubectl create
    - kubectl explain
    - kubectl create priorityclass high-priority --value=100000 --description="High priority" --global-default=false --dry-run=client -o yaml

    

- kubectl create

Available Commands:
  - clusterrole           Create a cluster role
  - clusterrolebinding    Create a cluster role binding for a particular cluster role
  - configmap             Create a config map from a local file, directory or literal value
  - cronjob               Create a cron job with the specified name
  - deployment            Create a deployment with the specified name
  - ingress               Create an ingress with the specified name
  - job                   Create a job with the specified name
  - namespace             Create a namespace with the specified name
  - poddisruptionbudget   Create a pod disruption budget with the specified name
  - priorityclass         Create a priority class with the specified name
  - quota                 Create a quota with the specified name
  - role                  Create a role with single rule
  - rolebinding           Create a role binding for a particular role or cluster role
  - secret                Create a secret using a specified subcommand
  - service               Create a service using a specified subcommand
  - serviceaccount        Create a service account with the specified name
  - token                 Request a service account token


1. Structure of manifest
2. Affinity (Pod (Affinity and AntiAffinity) and Node)
3. Selectors

# Installing Kubernetes

Kubernetes Version: 1.33.0-1.1 
Steps are as follows. Please do it on both master and worker nodes

1. Install Prerequestes

```bash 
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
```

```bash
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

```bash
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
```

```bash
sudo apt-cache madison kubeadm
sudo apt-get install -y kubelet=1.33.0-1.1 kubeadm=1.33.0-1.1 kubectl=1.33.0-1.1
sudo apt-mark hold kubelet kubeadm kubectl
```

# Initialize Control Plane Node (Master Node). Use the following options:

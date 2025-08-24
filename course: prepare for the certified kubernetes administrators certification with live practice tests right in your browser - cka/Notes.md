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
24. Practice Test - Multi Container PODs
25. Practice Test - Init Containers
26. Practice Test - Manual Scaling
27. Practice Test - HPA
28. Practice Test - Install VPA
29. Practice Test - Modifying CPU resources in VPA

### Cluster Maintenance
33. Practice Test - OS Upgrades
34. Practice Test - Cluster Upgrade Process
35. Practice Test - Backup and Restore Methods

### Security
36. Practice Test - View Certificate Details
37. Practice Test - Certificates API
38. Practice Test - KubeConfig
39. Practice Test - Role Based Access Controls
40. Practice Test - Cluster Roles
41. Practice Test - Service Accounts
42. Practice Test - Image Security
43. Practice Test - Security Contexts
44. Practice Test - Network Policies
45. Practice Test - Custom Resource Definition



### Install kubernetes "the kubeadm way"
Practice Tests - Cluster installation using kubeadm

### Ad Hoc Commands
  

- kubectl create
  - Available Commands:
    - clusterrole           Create a cluster role
    - clusterrolebinding    Create a cluster role binding for a particular cluster role
    - configmap             Create a config map from a local file, directory or literal value
    - cronjob               Create a cron job with the specified name
    - deployment            Create a deployment with the specified name
      - `kubectl create deploy manshu-deploy --image=nginx`
    - ingress               Create an ingress with the specified name
    - job                   Create a job with the specified name
    - namespace             Create a namespace with the specified name
      - `kubectl create ns manshu-namespace`
    - poddisruptionbudget   Create a pod disruption budget with the specified name
    - priorityclass         Create a priority class with the specified name
      - `kubectl create priorityclass custom-high-priority --value=100000 --description="High priority" --global-default=false --dry-run=client -o yaml`
    - quota                 Create a quota with the specified name
    - role                  Create a role with single rule
    - rolebinding           Create a role binding for a particular role or cluster role
    - secret                Create a secret using a specified subcommand
    - service               Create a service using a specified subcommand
    - serviceaccount        Create a service account with the specified name
    - token                 Request a service account token

- kubectl expose
- kubectl run
  - `kubectl run nginx --image=nginx`
- kubectl set
- kubectl explain
- kubectl get
- kubectl edit
- kubectl delete
- kubectl rollout
- kubectl scale
- kubectl autoscale
  - `kubectl autoscale deployment foo  --min=2 --max=10 --cpu-percent=80 -o yaml --dry-run=client`
  - `kubectl autoscale rc foo  --min=2 --max=10 --cpu-percent=80 -o yaml --dry-run=client`
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

- kubectl api-resources
- kubectl config
  - `kubectl config get-contexts` // list all context
  - `kubectl config get-contexts -o name` // list all context
  - `kubectl config current-context` // current contect
  - `kubectl config use-context cluster2` // to switch from one cluster to another




### Deployment Strategy in kubernetes
  - Rolling Update
  - Recreate

# Need further practice
10. Practice Tests - Node Affinity  
14. Practice Tests - Priority Classes
16. Practice Tests - Admission Controller
17. Practice Tests - Validating and Mutating Admission Controller
23. Practice Test - Secrets (secret types)
22. Practice Test - Env Variables (env vs envFrom)
30. Practice Test - HPA
34. Practice Test - Cluster Upgrade Process
35. Practice Test - Backup and Restore Methods
39. Practice Test - Role Based Access Controls


# Reference
- [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
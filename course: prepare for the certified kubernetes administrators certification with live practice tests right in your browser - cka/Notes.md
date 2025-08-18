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
18. Practice Test - Monitor Cluster Components
19. Practice Test - Managing Application Logs

### Application Life Cycle Management
20. Practice Test - Rolling Updates and Rollbacks
21. Practice Test - Commands and Arguments
22. Practice Test - Env Variables
23. Practice Test - Secrets
24. Practice Test - Multi Container PODs
25. Practice Test - Init Containers
26. Practice Test - Manual Scaling
27. Practice Test - HPA
28. Practice Test - Install VPA
29. Practice Test - Modifying CPU resources in VPA
30. Practice Test - HPA
31. Practice Test - Install VPA
32. Practice Test - Modifying CPU resources in VPA

### Install kubernetes "the kubeadm way"
Practice Tests - Cluster installation using kubeadm


# Important commands

- Imperative Commands
    - kubectl run nginx --image=nginx
    - kubectl delete
    - kubectl create
    - kubectl explain
    - kubectl create priorityclass high-priority --value=100000 --description="High priority" --global-default=false --dry-run=client -o yaml

    
- Suppose the exam gives you three clusters and ask to perform task in cluster2:
    - cluster1
    - cluster2
    - cluster3
```bash
kubectl config use-context cluster2
```
- Always double-check your current context
```bash
kubectl config current-context
```
- List down all context 
```bash
kubectl config get-contexts
kubectl config get-contexts -o name
```

- Deployment Strategy in kubernetes
  - Rolling Update
  - Recreate
  

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

- kubectl scale

1. Structure of manifest
2. Affinity (Pod (Affinity and AntiAffinity) and Node)
3. Selectors

# Need further practice
- nodeAffinity
- priorityClassName
- Admission Controller and Kube API server
- Validating and Mutating Admission Controllers 
- secret types
- env vs envFrom
- hpa

# Reference
- [Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
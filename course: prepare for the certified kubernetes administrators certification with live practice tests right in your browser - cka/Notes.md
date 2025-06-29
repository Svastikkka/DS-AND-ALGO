# Index
1. Pods                                                     DONE
2. Replicasets                                              DONE
3. Deployments                                              DONE
4. Namespaces                                               DONE
5. Services                                                 DONE
6. Imperative Commands (kubectl create/delete/top/run )     DONE
7. Manual Scheduling                                        DONE
8. Labels and Selectors
9. Taints and Toleration
10. Node Affinity
11. Resource Limits                                         DONE
12. Daemonsets
12. Static Pods                                             DONE
13. Priority Classes




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





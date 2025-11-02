Create a service messaging-service to expose the messaging application within the cluster on port 6379.

Use imperative commands.


Solution

Run the command: kubectl expose pod messaging --port=6379 --name messaging-service


---

Expose the hr-web-app created in the previous task as a service named hr-web-app-service, accessible on port 30082 on the nodes of the cluster.

The web application listens on port 8080.


Run the command: kubectl expose deployment hr-web-app --type=NodePort --port=8080 --name=hr-web-app-service --dry-run=client -o yaml > hr-web-app-service.yaml to generate a service definition file.

Now, in generated service definition file add the nodePort field with the given port number under the ports section and create a service.

---

Create a Horizontal Pod Autoscaler (HPA) with name webapp-hpa for the deployment named kkapp-deploy in the default namespace with the webapp-hpa.yaml file located under the root folder.
Ensure that the HPA scales the deployment based on CPU utilization, maintaining an average CPU usage of 50% across all pods.
Configure the HPA to cautiously scale down pods by setting a stabilization window of 300 seconds to prevent rapid fluctuations in pod count.

Note: The kkapp-deploy deployment is created for backend; you can check in the terminal.

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: kkapp-deploy
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 50
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
```


Deploy a Vertical Pod Autoscaler (VPA) with name analytics-vpa for the deployment named analytics-deployment in the default namespace.
The VPA should automatically adjust the CPU and memory requests of the pods to optimize resource utilization. Ensure that the VPA operates in Auto mode, allowing it to evict and recreate pods with updated resource requests as needed.

```yaml
kubectl create -n default -f - <<EOF
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: analytics-vpa
  namespace: default
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: analytics-deployment
  updatePolicy:
    updateMode: "Auto"
EOF
```
# minikube start
kubectl config use-context minikube

# Question: 1
kubectl create ns lima-control
kubectl create ns lima-workload
kubectl -n lima-workload create deployment department-deploy --image=nginx --replicas=2
kubectl -n lima-workload expose deployment department-deploy --name=department --port=80 --cluster-ip=None
kubectl -n lima-workload run section100 --image=nginx
kubectl -n lima-control create configmap dns-config \
  --from-literal=DNS_1="" \
  --from-literal=DNS_2="" \
  --from-literal=DNS_3="" \
  --from-literal=DNS_4=""

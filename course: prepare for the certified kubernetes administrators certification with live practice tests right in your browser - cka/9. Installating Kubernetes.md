1. Install the kubeadm and kubelet packages on the controlplane and node01 nodes.
Use the exact version of 1.33.0-1.1 for both.


```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl --system
```

```
sudo apt-get update

sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.33/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.33/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update


# To see the new version labels
sudo apt-cache madison kubeadm

sudo apt-get install -y kubelet=1.33.0-1.1 kubeadm=1.33.0-1.1 kubectl=1.33.0-1.1

sudo apt-mark hold kubelet kubeadm kubectl
```

2. Initialize Control Plane Node (Master Node). Use the following options:

- apiserver-advertise-address - Use the IP address allocated to eth0 on the controlplane node
- apiserver-cert-extra-sans - Set it to controlplane
- pod-network-cidr - Set to 172.17.0.0/16
- service-cidr - Set to 172.20.0.0/16

Once done, set up the default kubeconfig file and wait for node to be part of the cluster.


```

IP_ADDR=$(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
kubeadm init --apiserver-cert-extra-sans=controlplane --apiserver-advertise-address $IP_ADDR --pod-network-cidr=172.17.0.0/16 --service-cidr=172.20.0.0/16
```

```
mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config
```


3. Join node01 to the cluster using the join token

```bash
kubeadm token create --print-join-command

# ssh in node01
kubeadm join 192.168.75.188:6443 --token g2xyj2.v8uxlyulgqq3wast --discovery-token-ca-cert-hash sha256:d9ebcb509b9e9c656158207a68159b6660ee5dd6bfcd17dd6d327e1f62fb4e5d 
```

4. To install a network plugin, we will go with Flannel as the default choice. For inter-host communication, we will utilize the eth0 interface and update the Network field accordingly. Ensure that the Flannel manifest includes the appropriate options for this configuration. For detailed instructions, refer to the official documentation linked in the upper right corner above the terminal.


- Download the original YAML file and save it as kube-flannel.yml:
```
curl -LO https://raw.githubusercontent.com/flannel-io/flannel/v0.20.2/Documentation/kube-flannel.yml
```
- Open the kube-flannel.yml file using a text editor.

- We are using a custom PodCIDR (172.17.0.0/16) instead of the default 10.244.0.0/16 when bootstrapping the Kubernetes cluster. However, the Flannel manifest by default is configured to use 10.244.0.0/16 as its network, which does not align with the specified PodCIDR. To resolve this, we need to update the Network field in the kube-flannel-cfg ConfigMap to match the custom PodCIDR defined during cluster initialization.

```bash
net-conf.json: |
    {
      "Network": "10.244.0.0/16", # Update this to match the custom PodCIDR
      "Backend": {
        "Type": "vxlan"
      }
```

- Locate the args section within the kube-flannel container definition. It should look like this:
```bash
  args:
  - --ip-masq
  - --kube-subnet-mgr
```

- Add the additional argument - --iface=eth0 to the existing list of arguments.
- `kubectl apply -f kube-flannel.yml`
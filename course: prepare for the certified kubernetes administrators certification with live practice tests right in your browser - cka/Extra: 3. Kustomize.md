# Kustomize

- Kustomize is a Kubernetes-native configuration management tool that lets you customize YAML manifests — without templating.
- You can:
    - Reuse a common base configuration across environments.
    - Overlay (override) certain fields for environments like dev, staging, and prod.
    - Patch specific fields (replicas, images, labels, etc.).
```
app/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    ├── staging/
    │   └── kustomization.yaml
    └── prod/
        └── kustomization.yaml
```

# Commands

- Build YAML without applying: `kubectl kustomize ./overlays/staging`
- Apply directly to the cluster: `kubectl apply -k ./overlays/staging`
- Build and apply manually: `kubectl kustomize ./overlays/staging | kubectl apply -f -`
- Delete resources: `kubectl delete -k ./overlays/staging`
- Check base kustomize: `kubectl kustomize base`
- To check diffrence between deployed and new changes: `kubectl kustomize practice/app/overlays/dev | kubectl diff -f -`
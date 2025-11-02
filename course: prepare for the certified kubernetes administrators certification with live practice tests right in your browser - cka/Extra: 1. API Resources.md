NAME                                SHORTNAMES                 APIVERSION                                  NAMESPACED   KIND
bindings                                                       v1                                          true         Binding
componentstatuses                   cs                         v1                                          false        ComponentStatus
*configmaps*                          cm                         v1                                          true         ConfigMap
endpoints                           ep                         v1                                          true         Endpoints
events                              ev                         v1                                          true         Event
limitranges                         limits                     v1                                          true         LimitRange
*namespaces*                          ns                         v1                                          false        Namespace
*nodes*                               no                         v1                                          false        Node
*persistentvolumeclaims*              pvc                        v1                                          true         PersistentVolumeClaim
*persistentvolumes*                   pv                         v1                                          false        PersistentVolume
*pods*                                po                         v1                                          true         Pod
podtemplates                                                   v1                                          true         PodTemplate
*replicationcontrollers*              rc                         v1                                          true         ReplicationController
resourcequotas                      quota                      v1                                          true         ResourceQuota
secrets                                                        v1                                          true         Secret
*serviceaccounts*                     sa                         v1                                          true         ServiceAccount
*services*                            svc                        v1                                          true         Service
challenges                                                     acme.cert-manager.io/v1                     true         Challenge
orders                                                         acme.cert-manager.io/v1                     true         Order
mutatingwebhookconfigurations                                  admissionregistration.k8s.io/v1             false        MutatingWebhookConfiguration
validatingadmissionpolicies                                    admissionregistration.k8s.io/v1             false        ValidatingAdmissionPolicy
validatingadmissionpolicybindings                              admissionregistration.k8s.io/v1             false        ValidatingAdmissionPolicyBinding
validatingwebhookconfigurations                                admissionregistration.k8s.io/v1             false        ValidatingWebhookConfiguration
*agents*                              agent                      agent.k8s.elastic.co/v1alpha1               true         Agent
entitlements                                                   anthos.gke.io/v1alpha1                      false        Entitlement
*customresourcedefinitions*           crd,crds                   apiextensions.k8s.io/v1                     false        CustomResourceDefinition
apiservices                                                    apiregistration.k8s.io/v1                   false        APIService
apmservers                          apm                        apm.k8s.elastic.co/v1                       true         ApmServer
applications                        app                        app.k8s.io/v1beta1                          true         Application
controllerrevisions                                            apps/v1                                     true         ControllerRevision
*daemonsets*                          ds                         apps/v1                                     true         DaemonSet
*deployments*                         deploy                     apps/v1                                     true         Deployment
*replicasets*                         rs                         apps/v1                                     true         ReplicaSet
*statefulsets*                        sts                        apps/v1                                     true         StatefulSet
selfsubjectreviews                                             authentication.k8s.io/v1                    false        SelfSubjectReview
tokenreviews                                                   authentication.k8s.io/v1                    false        TokenReview
localsubjectaccessreviews                                      authorization.k8s.io/v1                     true         LocalSubjectAccessReview
selfsubjectaccessreviews                                       authorization.k8s.io/v1                     false        SelfSubjectAccessReview
selfsubjectrulesreviews                                        authorization.k8s.io/v1                     false        SelfSubjectRulesReview
subjectaccessreviews                                           authorization.k8s.io/v1                     false        SubjectAccessReview
allowlistedv2workloads                                         auto.gke.io/v1                              false        AllowlistedV2Workload
allowlistedworkloads                                           auto.gke.io/v1                              false        AllowlistedWorkload
allowlistsynchronizers                                         auto.gke.io/v1                              false        AllowlistSynchronizer
workloadallowlists                                             auto.gke.io/v1                              false        WorkloadAllowlist
*horizontalpodautoscalers*            hpa                        autoscaling/v2                              true         HorizontalPodAutoscaler
multidimpodautoscalers              mpa                        autoscaling.gke.io/v1beta1                  true         MultidimPodAutoscaler
metrics                                                        autoscaling.internal.knative.dev/v1alpha1   true         Metric
podautoscalers                      kpa,pa                     autoscaling.internal.knative.dev/v1alpha1   true         PodAutoscaler
elasticsearchautoscalers            esa                        autoscaling.k8s.elastic.co/v1alpha1         true         ElasticsearchAutoscaler
verticalpodautoscalers              vpa                        autoscaling.k8s.io/v1                       true         VerticalPodAutoscaler
provisioningrequests                provreq,provreqs           autoscaling.x-k8s.io/v1                     true         ProvisioningRequest
cronjobs                            cj                         batch/v1                                    true         CronJob
jobs                                                           batch/v1                                    true         Job
beats                               beat                       beat.k8s.elastic.co/v1beta1                 true         Beat
images                                                         caching.internal.knative.dev/v1alpha1       true         Image
*certificaterequests*                 cr,crs                     cert-manager.io/v1                          true         CertificateRequest
*certificates*                        cert,certs                 cert-manager.io/v1                          true         Certificate
clusterissuers                                                 cert-manager.io/v1                          false        ClusterIssuer
issuers                                                        cert-manager.io/v1                          true         Issuer
certificatesigningrequests          csr                        certificates.k8s.io/v1                      false        CertificateSigningRequest
ciliumendpoints                     cep,ciliumep               cilium.io/v2                                true         CiliumEndpoint
ciliumendpointslices                ces                        cilium.io/v2alpha1                          false        CiliumEndpointSlice
ciliumexternalworkloads             cew                        cilium.io/v2                                false        CiliumExternalWorkload
ciliumidentities                    ciliumid                   cilium.io/v2                                false        CiliumIdentity
ciliumlocalredirectpolicies         clrp                       cilium.io/v2                                true         CiliumLocalRedirectPolicy
ciliumnodes                         cn,ciliumn                 cilium.io/v2                                false        CiliumNode
clickhousekeeperinstallations       chk                        clickhouse-keeper.altinity.com/v1           true         ClickHouseKeeperInstallation
clickhouseinstallations             chi                        clickhouse.altinity.com/v1                  true         ClickHouseInstallation
clickhouseinstallationtemplates     chit                       clickhouse.altinity.com/v1                  true         ClickHouseInstallationTemplate
clickhouseoperatorconfigurations    chopconf                   clickhouse.altinity.com/v1                  true         ClickHouseOperatorConfiguration
backendconfigs                      bc                         cloud.google.com/v1                         true         BackendConfig
computeclasses                      cc,ccs                     cloud.google.com/v1                         false        ComputeClass
leases                                                         coordination.k8s.io/v1                      true         Lease
gcpdatasources                      gds                        datalayer.gke.io/v1                         true         GCPDataSource
endpointslices                                                 discovery.k8s.io/v1                         true         EndpointSlice
elasticsearches                     es                         elasticsearch.k8s.elastic.co/v1             true         Elasticsearch
enterprisesearches                  ent                        enterprisesearch.k8s.elastic.co/v1          true         EnterpriseSearch
cloudeventsources                                              eventing.keda.sh/v1alpha1                   true         CloudEventSource
clustercloudeventsources                                       eventing.keda.sh/v1alpha1                   false        ClusterCloudEventSource
events                              ev                         events.k8s.io/v1                            true         Event
flowschemas                                                    flowcontrol.apiserver.k8s.io/v1             false        FlowSchema
prioritylevelconfigurations                                    flowcontrol.apiserver.k8s.io/v1             false        PriorityLevelConfiguration
gatewayclasses                      gc                         gateway.networking.k8s.io/v1                false        GatewayClass
gateways                            gtw                        gateway.networking.k8s.io/v1                true         Gateway
grpcroutes                                                     gateway.networking.k8s.io/v1                true         GRPCRoute
httproutes                                                     gateway.networking.k8s.io/v1                true         HTTPRoute
referencegrants                     refgrant                   gateway.networking.k8s.io/v1beta1           true         ReferenceGrant
highavailabilityapplications                                   ha.gke.io/v1                                true         HighAvailabilityApplication
httpscaledobjects                   httpso                     http.keda.sh/v1alpha1                       true         HTTPScaledObject
memberships                                                    hub.gke.io/v1                               false        Membership
capacityrequests                    capreq                     internal.autoscaling.gke.io/v1              true         CapacityRequest
clustertriggerauthentications       cta,clustertriggerauth     keda.sh/v1alpha1                            false        ClusterTriggerAuthentication
scaledjobs                          sj                         keda.sh/v1alpha1                            true         ScaledJob
scaledobjects                       so                         keda.sh/v1alpha1                            true         ScaledObject
triggerauthentications              ta,triggerauth             keda.sh/v1alpha1                            true         TriggerAuthentication
kibanas                             kb                         kibana.k8s.elastic.co/v1                    true         Kibana
serviceprofiles                     sp                         linkerd.io/v1alpha2                         true         ServiceProfile
logstashes                          ls                         logstash.k8s.elastic.co/v1alpha1            true         Logstash
elasticmapsservers                  ems                        maps.k8s.elastic.co/v1alpha1                true         ElasticMapsServer
nodes                                                          metrics.k8s.io/v1beta1                      false        NodeMetrics
pods                                                           metrics.k8s.io/v1beta1                      true         PodMetrics
clusternodemonitorings                                         monitoring.googleapis.com/v1                false        ClusterNodeMonitoring
clusterpodmonitorings                                          monitoring.googleapis.com/v1                false        ClusterPodMonitoring
clusterrules                                                   monitoring.googleapis.com/v1                false        ClusterRules
globalrules                                                    monitoring.googleapis.com/v1                false        GlobalRules
operatorconfigs                                                monitoring.googleapis.com/v1                true         OperatorConfig
podmonitorings                                                 monitoring.googleapis.com/v1                true         PodMonitoring
rules                                                          monitoring.googleapis.com/v1                true         Rules
egressnatpolicies                                              networking.gke.io/v1                        false        EgressNATPolicy
frontendconfigs                                                networking.gke.io/v1beta1                   true         FrontendConfig
gcpbackendpolicies                                             networking.gke.io/v1                        true         GCPBackendPolicy
gcpgatewaypolicies                                             networking.gke.io/v1                        true         GCPGatewayPolicy
gcproutingextensions                                           networking.gke.io/v1                        true         GCPRoutingExtension
gcptrafficdistributionpolicies                                 networking.gke.io/v1                        true         GCPTrafficDistributionPolicy
gcptrafficextensions                                           networking.gke.io/v1                        true         GCPTrafficExtension
gkeiproutes                                                    networking.gke.io/v1                        true         GKEIPRoute
gkenetworkparamsets                                            networking.gke.io/v1                        false        GKENetworkParamSet
healthcheckpolicies                                            networking.gke.io/v1                        true         HealthCheckPolicy
lbpolicies                                                     networking.gke.io/v1                        true         LBPolicy
managedcertificates                 mcrt                       networking.gke.io/v1                        true         ManagedCertificate
networkloggings                     nl                         networking.gke.io/v1alpha1                  false        NetworkLogging
networks                                                       networking.gke.io/v1                        false        Network
nodetopologies                      tp                         networking.gke.io/v1                        false        NodeTopology
redirectservices                    rds                        networking.gke.io/v1alpha1                  true         RedirectService
serviceattachments                                             networking.gke.io/v1                        true         ServiceAttachment
servicefunctionchains                                          networking.gke.io/v1                        false        ServiceFunctionChain
servicenetworkendpointgroups        svcneg                     networking.gke.io/v1beta1                   true         ServiceNetworkEndpointGroup
trafficselectors                                               networking.gke.io/v1                        false        TrafficSelector
certificates                        kcert                      networking.internal.knative.dev/v1alpha1    true         Certificate
clusterdomainclaims                 cdc                        networking.internal.knative.dev/v1alpha1    false        ClusterDomainClaim
ingresses                           kingress,king              networking.internal.knative.dev/v1alpha1    true         Ingress
serverlessservices                  sks                        networking.internal.knative.dev/v1alpha1    true         ServerlessService
ingressclasses                                                 networking.k8s.io/v1                        false        IngressClass
*ingresses*                           ing                        networking.k8s.io/v1                        true         Ingress
networkpolicies                     netpol                     networking.k8s.io/v1                        true         NetworkPolicy
gcpresourceallowlists                                          node.gke.io/v1                              false        GCPResourceAllowlist
runtimeclasses                                                 node.k8s.io/v1                              false        RuntimeClass
updateinfos                         updinf                     nodemanagement.gke.io/v1alpha1              true         UpdateInfo
vlogs                                                          operator.victoriametrics.com/v1beta1        true         VLogs
vmagents                                                       operator.victoriametrics.com/v1beta1        true         VMAgent
vmalertmanagerconfigs                                          operator.victoriametrics.com/v1beta1        true         VMAlertmanagerConfig
vmalertmanagers                     vma                        operator.victoriametrics.com/v1beta1        true         VMAlertmanager
vmalerts                                                       operator.victoriametrics.com/v1beta1        true         VMAlert
vmauths                                                        operator.victoriametrics.com/v1beta1        true         VMAuth
vmclusters                                                     operator.victoriametrics.com/v1beta1        true         VMCluster
vmnodescrapes                                                  operator.victoriametrics.com/v1beta1        true         VMNodeScrape
vmpodscrapes                                                   operator.victoriametrics.com/v1beta1        true         VMPodScrape
vmprobes                                                       operator.victoriametrics.com/v1beta1        true         VMProbe
vmrules                                                        operator.victoriametrics.com/v1beta1        true         VMRule
vmscrapeconfigs                                                operator.victoriametrics.com/v1beta1        true         VMScrapeConfig
vmservicescrapes                                               operator.victoriametrics.com/v1beta1        true         VMServiceScrape
vmsingles                                                      operator.victoriametrics.com/v1beta1        true         VMSingle
vmstaticscrapes                                                operator.victoriametrics.com/v1beta1        true         VMStaticScrape
vmusers                                                        operator.victoriametrics.com/v1beta1        true         VMUser
*poddisruptionbudgets*                pdb                        policy/v1                                   true         PodDisruptionBudget
authorizationpolicies               authzpolicy                policy.linkerd.io/v1alpha1                  true         AuthorizationPolicy
egressnetworks                                                 policy.linkerd.io/v1alpha1                  true         EgressNetwork
httplocalratelimitpolicies                                     policy.linkerd.io/v1alpha1                  true         HTTPLocalRateLimitPolicy
httproutes                                                     policy.linkerd.io/v1beta3                   true         HTTPRoute
meshtlsauthentications              meshtlsauthn               policy.linkerd.io/v1alpha1                  true         MeshTLSAuthentication
networkauthentications              netauthn,networkauthn      policy.linkerd.io/v1alpha1                  true         NetworkAuthentication
serverauthorizations                saz,serverauthz,srvauthz   policy.linkerd.io/v1beta1                   true         ServerAuthorization
servers                             srv                        policy.linkerd.io/v1beta3                   true         Server
clusterrolebindings                                            rbac.authorization.k8s.io/v1                false        ClusterRoleBinding
clusterroles                                                   rbac.authorization.k8s.io/v1                false        ClusterRole
rolebindings                                                   rbac.authorization.k8s.io/v1                true         RoleBinding
roles                                                          rbac.authorization.k8s.io/v1                true         Role
*priorityclasses*                     pc                         scheduling.k8s.io/v1                        false        PriorityClass
gkeclustertrustbundles                                         security.cloud.google.com/v1                false        GKEClusterTrustBundle
trustconfigs                                                   security.cloud.google.com/v1                false        TrustConfig
workloadcertificateconfigs                                     security.cloud.google.com/v1                false        WorkloadCertificateConfig
configurations                      config,cfg                 serving.knative.dev/v1                      true         Configuration
domainmappings                      dm                         serving.knative.dev/v1beta1                 true         DomainMapping
revisions                           rev                        serving.knative.dev/v1                      true         Revision
routes                              rt                         serving.knative.dev/v1                      true         Route
services                            kservice,ksvc              serving.knative.dev/v1                      true         Service
volumesnapshotclasses               vsclass,vsclasses          snapshot.storage.k8s.io/v1                  false        VolumeSnapshotClass
volumesnapshotcontents              vsc,vscs                   snapshot.storage.k8s.io/v1                  false        VolumeSnapshotContent
volumesnapshots                     vs                         snapshot.storage.k8s.io/v1                  true         VolumeSnapshot
stackconfigpolicies                 scp                        stackconfigpolicy.k8s.elastic.co/v1alpha1   true         StackConfigPolicy
csidrivers                                                     storage.k8s.io/v1                           false        CSIDriver
csinodes                                                       storage.k8s.io/v1                           false        CSINode
csistoragecapacities                                           storage.k8s.io/v1                           true         CSIStorageCapacity
*storageclasses*                      sc                         storage.k8s.io/v1                           false        StorageClass
volumeattachments                                              storage.k8s.io/v1                           false        VolumeAttachment
audits                                                         warden.gke.io/v1                            false        Audit
externalworkloads                                              workload.linkerd.io/v1beta1                 true         ExternalWorkload
Create a new user called john. Grant him access to the cluster using a csr named john-developer. Create a role developer which should grant John the permission to create, list, get, update and delete pods in the development namespace . The private key exists in the location: /root/CKA/john.key and csr at /root/CKA/john.csr.


Important Note: As of kubernetes 1.19, the CertificateSigningRequest object expects a signerName.

Please refer to the documentation to see an example. The documentation tab is available at the top right of the terminal.



---


Modify the existing web-gateway on cka5673 namespace to handle HTTPS traffic on port 443 for kodekloud.com, using a TLS certificate stored in a secret named kodekloud-tls.


Is the web gateway configured to listen on the hostname kodekloud.com?

Is the HTTPS listener configured with the correct TLS certificate?
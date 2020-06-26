from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import padding
import json
import hashlib
import base64
def check_json(json_text):
    dictionary = json.loads(json_text)
    sha = hashlib.sha512()
    pem_cert = open('cert.pem').read().encode('UTF-8')
    public_key = x509.load_pem_x509_certificate(pem_cert,default_backend()).public_key()
    message = json.dumps(dictionary['response']).encode()
    #nombre = base64.b64decode(request.json['name'].encode()).decode('UTF-8')
    public_key.verify(
        base64.b64decode(dictionary['signature'].encode()),
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    #assert(sha.hexdigest()==dictionary['signature'])

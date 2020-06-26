from cryptography import x509
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import base64
def get_serial_number():
    return x509.random_serial_number()
def sign_json(json):
    pem_private_key = open('pk.pem').read().encode('UTF-8')
    private_key = serialization.load_pem_private_key(
    	    pem_private_key,
    	    password='1234'.encode('UTF-8'),
    	    backend=default_backend()
    )
    signature = private_key.sign(
        json,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode()

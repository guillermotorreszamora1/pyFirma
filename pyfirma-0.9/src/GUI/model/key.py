from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization,hashes
import os
from model.cert_storage import CERT_DIR
def generate_key(password,nif,strength=4096):
    private_key =  rsa.generate_private_key(public_exponent=65537,
        key_size=strength,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding = serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode('UTF-8'))).decode()
    try:
        os.mkdir(CERT_DIR+nif)
    except:
        pass
    public_file = open(CERT_DIR+nif+'/public.pem','w')
    public_file.write(public_pem)
    private_file = open(CERT_DIR+nif+'/private.pem','w')
    private_file.write(private_pem)
    return public_pem

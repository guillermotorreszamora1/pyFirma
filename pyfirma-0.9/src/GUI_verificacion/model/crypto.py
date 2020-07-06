from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.x509.oid import NameOID
from endesive.pdf import cms
from endesive import pdf
from asn1crypto import cms as parser
import datetime
def load_CA(password,private_key_file,certificate_file):
    f = open(private_key_file)
    pem = f.read().encode('UTF-8')
    pk = load_pem_private_key(pem,password=password.encode('UTF-8'),backend=default_backend())
    f = open(certificate_file)
    pem_data = f.read().encode('UTF-8')
    cert = x509.load_pem_x509_certificate(pem_data,default_backend())
    return pk,cert
def certificate(public_key,name,serial_number):
    ca_private_key, cert = load_CA('1234','/usr/share/pyfirma/server/pk.pem','/usr/share/pyfirma/cert.pem')
    root_cert = cert
    issuer = root_cert.issuer
    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,name)])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        serialization.load_pem_public_key(public_key.encode(),backend=default_backend())
    ).serial_number(
        serial_number
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=3650)
    ).add_extension(
        extension=x509.KeyUsage(
            digital_signature=True,key_encipherment=True,
            content_commitment=True,data_encipherment=False,
            key_agreement=False,encipher_only=False,
            decipher_only=False,key_cert_sign=False,
            crl_sign=False
        ),
        critical=True
    ).add_extension(
        extension=x509.BasicConstraints(ca=False,path_length=None),
        critical=True
    ).add_extension(
        extension=x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_private_key.public_key()),
        critical=False
    ).sign(
        private_key=ca_private_key,
        algorithm=hashes.SHA512(),
        backend=default_backend()
    )
    return cert.public_bytes(serialization.Encoding.PEM).decode()

import datetime
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.x509.oid import NameOID
from cryptography import x509
def create_ca(password,private_key_fn,certificate_fn,strength,name):
    ca_pk = rsa.generate_private_key(public_exponent=65537,
        key_size=strength,
        backend=default_backend()
    )
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME,name)])
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        ca_pk.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=3650)
    ).add_extension(
        extension=x509.BasicConstraints(ca=True,path_length=None),
        critical=True
    ).add_extension(
        extension=x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_pk.public_key()),
        critical=False
    ).sign(
        private_key=ca_pk,
        algorithm=hashes.SHA512(),
        backend=default_backend()
    )
    pk_pem = ca_pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode('UTF-8')))
    print(type(pk_pem))
    f = open(private_key_fn,'wb')
    f.write(pk_pem)
    f.close()
    print(type(cert.public_bytes(serialization.Encoding.PEM)))
    f = open(certificate_fn,'wb')
    f.write(cert.public_bytes(serialization.Encoding.PEM))

create_ca(contrasena,'pk.pem','cert.pem',8192,nombre_ca)

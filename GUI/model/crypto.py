from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.x509.oid import NameOID
from asn1crypto import cms as parser
from endesive import pdf
from endesive.pdf import cms
from cryptography.hazmat.primitives.serialization import load_pem_private_key
def check_cert(pem_cert,n_serie):
    cert = x509.load_pem_x509_certificate(pem_cert.encode(),backend=default_backend())
    assert(cert.serial_number==n_serie)
def sign_doc(filename,user,password):
    file = open(filename,'rb').read()
    cert = x509.load_pem_x509_certificate(user.load_cert().encode(),backend=default_backend())
    subject = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
    private_key = serialization.load_pem_private_key(
        user.load_private_key().encode(),
        password=password.encode('UTF-8'),
        backend=default_backend()
    )
    signature = cms.sign(file,{'contact':subject,'location':'',
        'reason':'','signingdate':'','signaturebox':(350, 50, 550, 150),
        'signature':'Firmado por '+subject},private_key,cert,[],"sha512")
    pdf_signed = file + signature
    name ,serial_number = check_signature(pdf_signed)
    user_data = "Nombre:"+user.nombre+"\nNIF:"+user.nif
    print(name)
    print(user_data)
    assert name==user_data
    assert serial_number == user.n_serie
    return pdf_signed
def check_signature(pdf_stream):
    root_cert = x509.load_pem_x509_certificate(open('cert.pem').read().encode(),backend=default_backend())
    (a,b,c) = pdf.verify(pdf_stream,[root_cert.public_bytes(serialization.Encoding.PEM)])
    print((a,b,c))
    assert (a,b,c)==(True,True,True)
    n = pdf_stream.find(b"/ByteRange")
    start = pdf_stream.find(b"[", n)
    stop = pdf_stream.find(b"]", start)
    assert n != -1 and start != -1 and stop != -1
    br = [int(i, 10) for i in pdf_stream[start + 1 : stop].split()]
    contents = pdf_stream[br[0] + br[1] + 1 : br[2] - 1]
    bcontents = bytes.fromhex(contents.decode("utf8"))
    data1 = pdf_stream[br[0] : br[0] + br[1]]
    data2 = pdf_stream[br[2] : br[2] + br[3]]
    signedData = data1 + data2
    parsedSignedData = parser.ContentInfo.load(bcontents)['content']
    print("NAME")
    name = parsedSignedData['certificates'][0].native['tbs_certificate']['subject']['common_name']
    #print(parsedSignedData['certificates'][0].native['tbs_certificate']['issuer']['common_name'])
    serial_number = parsedSignedData['certificates'][0].native['tbs_certificate']['serial_number']
    return name,serial_number

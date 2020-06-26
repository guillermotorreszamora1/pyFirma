import os
import json
def list_pending_cert():
    list_nif = []
    for folder in os.listdir('cert_storage'):
        if not 'cert.pem' in os.listdir('cert_storage/'+folder):
            list_nif.append(folder)
    list_nif.sort()
    return list_nif
def list_accepted_cert():
    list_nif = []
    for folder in os.listdir('cert_storage'):
        if 'cert.pem' in os.listdir('cert_storage/'+folder):
            list_nif.append(folder)
    list_nif.sort()
    return list_nif
class User():
    def __init__(self,nombre,nif,n_serie):
        self.nombre = nombre
        self.nif = nif
        self.n_serie = n_serie
    def load(nif):
        file = open('cert_storage/'+nif+'/data.txt')
        dic = json.loads(file.read())
        return User(nombre=dic['nombre'],nif=dic['nif'],n_serie=dic['n_serie'])
    def save(self):
        dic = {}
        dic['nombre'] = self.nombre
        dic['nif'] = self.nif
        dic['n_serie'] = self.n_serie
        try:
            os.mkdir('cert_storage/'+self.nif)
        except:
            pass
        file = open('cert_storage/'+self.nif+'/data.txt','w')
        file.write(json.dumps(dic))
    def save_cert(self,cert):
        file = open('cert_storage/'+self.nif+'/cert.pem','w')
        file.write(cert)
    def load_cert(self):
        file = open('cert_storage/'+self.nif+'/cert.pem')
        return file.read()
    def load_private_key(self):
        file = open('cert_storage/'+self.nif+'/private.pem')
        return file.read()
    def __str__(self):
        return self.nif+" "+self.nombre
    def __repr__(self):
        return str(self)

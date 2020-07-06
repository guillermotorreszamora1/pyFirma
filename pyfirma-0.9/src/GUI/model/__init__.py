import model.nif
import model.key
import model.signature
import model.network
import model.pdf
import model.cert_storage
import model.crypto
import os
from pathlib import Path
home = str(Path.home())
def prepare():
    if not '.pyfirma' in os.listdir(home):
        os.mkdir(home+'/.pyfirma')
    if not 'cert_storage' in os.listdir(home+'/.pyfirma'):
        os.mkdir(home+'/.pyfirma/cert_storage')

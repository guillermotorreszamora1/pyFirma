# pyFirma
Implementación de un sistema de firma electronica en Python
Este programa implementa un sistema de firma electronica para documentos PDF.
Consta de tres programas:
  -pyfirma-server: servidor necesario para registrar las peticiones de certificado.
  -pyfirma-verificacion: aplicación para la verificación de identidad desde la oficina de certificación(presencial).
  -pyfirma: aplicación para el usuario final que gestiona los certificados y permite firmar y verificar firmas.


Construcion de los paquetes(Actualmente solo es posible para distribuciones linux basadas en Debian):
  1)Para empaquetarlo primero hay que installar las dependencias de compilacion(paquetes debian) especificadas en Debian/control:
    -debhelper
    -python3-dev
    -dh-virtualenv
    -python3
    -python3-pip
    -python3-setuptools
    -swig
    -python3-venv
  2)Ademas hay que instalar a traves de pip cryptography.
  3)Despues se configurara el programa:
    3.1) en el fichero src/create_ca.py especificando contrasena y nombre_ca(linea 48).
    3.2) en src/GUI/model/network.py especificando API_ENDPOINT como dirreción a la que se conectara la aplicación de usuario para pedir el certificado.
    3.3) en src/server/__init__.py especificando URL_PREFIX con el prefijo necesario. Es decir si API_ENDPOINT es 'example.com/firma_digital/' URL_PREFIX  es '/firma_digital'.
    3.4) Ejecutar create_ca.py para generar el certificado raiz y la clave privada de la entidad certificadora.
  4) Empaquetar
    dpkg-buildpackage -us -uc -tc
El empaquetado genera tres paquetes.
  pyfirma-server: contiene el programa pyfirma-server y pyfirma-verificacion asi como la clave privada.
  pyfima-user: contiene el programa pyfirma-user
  pyfirma-common: contiene ficheros necesarios para ambos programas, en particular el certificado raiz y un entorno virtual python.

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from cryptography import x509
import qrcode
from reportlab.lib.utils import ImageReader
def save_pdf(filename,identifier):
    rv = BytesIO()
    c=canvas.Canvas(filename,pagesize= A4)
    c.drawString(70,700,"Solicitud de certificado digital(Verificacion de identidad)")
    c.drawString(70,685,"Presente este documento junto con su DNI en una oficina de Registro")
    qrcode.make(identifier).save(rv)
    c.drawImage(ImageReader(rv),A4[0]/4,A4[1]/4,width=260,height=260)
    c.showPage()
    c.save()

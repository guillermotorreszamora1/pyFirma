caractes_de_control = "TRWAGMYFPDXBNJZSQVHLCKE"
def verificar(nif):
    if len(nif)!=9:
        return False
    if nif[0]=='X':
        nif = '0' + nif[1:]
    if nif[0]=='Y':
        nif = '1' + nif[1:]
    if nif[0]=='Z':
        nif = '2' + nif[1:]
    try:
        numero = int(nif[:-1])
    except:
        return False
    ctrl = nif[-1]
    if ctrl != caractes_de_control[numero%23]:
        return False
    return True

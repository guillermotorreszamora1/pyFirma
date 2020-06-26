import model
import view
def list_cert_loader(event,gui):
    user_list = []
    nif_list = model.cert_storage.list_pending_cert()
    for nif in nif_list:
        u = model.cert_storage.User.load(nif)
        user_list.append(u)
    gui.resize_and_set(view.list_pending_cert.list_pending_cert(user_list))

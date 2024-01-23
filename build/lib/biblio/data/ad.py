from flask import g

from ldap3 import Server, Connection, NTLM, ALL
from biblio.credentials.credentials import active_directory


server = Server(f'{active_directory.IP}', 389, get_info=ALL)           
    
def connectAD(username, password):
    if 'ad' not in g:
        g.ad = Connection(server,  user=f"{active_directory.DOMAIN}.{active_directory.NAME}\\"+username, password=password,  authentication=NTLM)
    return g.ad

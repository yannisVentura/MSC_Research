from socket import *
import sys
from log import Log

print(format(sys.argv[0]))
log = Log('server' + format(sys.argv[1]) + ".log")

TAILLE_TAMPON = 256

if len(sys.argv) != 2:
    print("Usage: {} <port>".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)

sock = socket(AF_INET, SOCK_DGRAM)

# Liaison de la socket à toutes les IP possibles de la machine
sock.bind(('', int(sys.argv[1])))
print("Serveur en attente sur le port " + sys.argv[1], file=sys.stderr)
log.write_info("Server liscten to " + sys.argv[1])

while True:
    try:
        log.write_info("Server listening...")
        # Récupération de la requête du client
        requete = sock.recvfrom(TAILLE_TAMPON)
        # Extraction du message et de l’adresse sur le client
        (mess, adr_client) = requete
        ip_client, port_client = adr_client

        print("Requête provenant de {}. Longueur = {}". \
              format(ip_client, len(mess)), file=sys.stderr)
        log.write_info("Request receive from" + ip_client)
        # Construction de la réponse
        reponse = mess.decode().upper()
        log.write_info("Send response to " + ip_client)
        # Envoi de la réponse au client
        sock.sendto(reponse.encode(), adr_client)
    except KeyboardInterrupt:
        log.write_critical("KeyboardInterrupt")
        break
    except OSError:
        log.write_error("Error message to long :( so bad !!")
        break
sock.close()
print("Arrêt du serveur", file=sys.stderr)
log.write_warning("Server stop")
sys.exit(0)

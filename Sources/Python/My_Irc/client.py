from socket import *
import sys
from log import Log

TAILLE_TAMPON = 256
log = Log("client" + format(sys.argv[1]) + ".log")

if len(sys.argv) != 3:
    print("Usage: {} <ip> <port>".format(sys.argv[0]), file=sys.stderr)
    log.write_critical("Usage: {} <ip> <port>".format(sys.argv[0]))
    log.write_critical("Exit 1")
    sys.exit(1)

with socket(AF_INET, SOCK_DGRAM) as sock:
    while True:
        try:
            log.write_info("Initialise client on " + sys.argv[1])
            # Remarque : pas besoin de bind car le port local est choisi par le système
            mess = "this is a simple message from me "

            while True:
                try:
                    # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
                    log.write_info(sys.argv[1] + "send :" + mess + "to server")
                    sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
                except KeyboardInterrupt:
                    break

            # Réception de la réponse du serveur et décodage de bytes en str
            reponse, _ = sock.recvfrom(TAILLE_TAMPON)
            print("Réponse = " + reponse.decode())
            log.write_info("receive response : " + reponse.decode())
        except KeyboardInterrupt:
            log.write_critical("KeyboardInterrupt")
            break

log.write_warning("Client close")
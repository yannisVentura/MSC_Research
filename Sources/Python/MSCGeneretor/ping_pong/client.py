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
    mess = "Initialise communication..."
    sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
    reponse, address = sock.recvfrom(TAILLE_TAMPON)
    server_adress = str(address[0])
    ip = str(address[1])
    print("the server adress is : " + server_adress)
    print("listening on " + ip)
    log.write_info('The server address is ' + server_adress)
    log.write_info('Server Ip : ' + ip)
    while True:
        try:
            # Remarque : pas besoin de bind car le port local est choisi par le système
            sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
            reponse, address = sock.recvfrom(TAILLE_TAMPON)
            mess = "this is a simple test message "
            # Envoi de la requête au serveur (ip, port) après encodage de str en bytes
            log.write_info(sys.argv[1] + "send :" + mess + "to " + server_adress)
            sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
            # Réception de la réponse du serveur et décodage de bytes en str
            print("Réponse = " + reponse.decode())
            log.write_info("receive response : " + reponse.decode() + "to " + server_adress)
        except KeyboardInterrupt:
            log.write_critical("KeyboardInterrupt")
            break

log.write_warning("Client close")

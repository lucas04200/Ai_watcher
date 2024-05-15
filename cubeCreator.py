import socket
import time

def send_data(data, host, port):
    # Création du socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connexion au serveur et envoi des données
        sock.connect((host, port))
        sock.sendall(data.encode("utf-8"))
        print(f"Envoyé : {data}")
    finally:
        sock.close()

host, port = "127.0.0.1", 25002  # IP et port du serveur Unity
data = "1"
send_data(data, host, port)
import socket
import select
import tkinter

maFenetre = tkinter.Tk()

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 9000
serveur.bind((host, port))
serveur.listen(4)
client_connecté = True
socket_objs = [serveur]

print("Bienvenue dans le chat !")

while client_connecté:
    
    liste_lu, liste_acce_Ecrit, exception = select.select(socket_objs, [], socket_objs)

    for socket_obj in liste_lu:

        if socket_obj is serveur:
            client, adresse = serveur.accept()
            print(f"l'object client socket: {client} - adresse: {adresse}")
            socket_objs.append(client)
        
        else: 
            données_reçues = socket_obj.recv(128).decode("utf-8")
            if données_reçues:
                print(données_reçues)

            else:
                socket_objs.remove(socket_obj)
                print("1 utilisateur est parti")
                print(f"{len(socket_objs) - 1} enculés restants")
import socket
import cryptocode

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455

    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))
    print("Serveur UDP à l'écoute...")

    while True:
        data, addr = server.recvfrom(1024)
        print(f"Message du client codé: {data}")

        data = cryptocode.decrypt(data.decode(), "12345")
        if data == "!EXIT":
            print("Client disconnected.")
            break

        print(f"Message du client décodé: {data}")

        data = data.upper()
        data = cryptocode.encrypt(data, "12345")
        server.sendto(data.encode(), addr)
import socket
import cryptocode

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)

    """ Creating the UDP socket """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("Entrez un message: ")

        if data == "!EXIT":
            data = cryptocode.encrypt(data, "12345")
            client.sendto(data, addr)
            print("Disconneted from the server.")
            break

        data = cryptocode.encrypt(data, "12345")
        client.sendto(data.encode(), addr)

        data, addr = client.recvfrom(1024)
        data = cryptocode.decrypt(data.decode(), "12345")
        print(f"Message du serveur: {data}")
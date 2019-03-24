import socket as skt

with skt.socket() as client:
    client.bind(("", 2075))
    client.listen()
    serv, addr = client.accept()
    text = serv.recv(1024)
    print(text)

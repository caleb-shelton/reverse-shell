import socket

s = socket.socket()

host = "127.0.0.1"
port = 9998


s.bind((host, port))

s.listen(2)


client, add = s.accept()


cmd = input("user@{}:~$ ".format(host))
while cmd != "q":
    client.send(cmd.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print(response)
    cmd = input("fixoc-#")

import socket

s = socket.socket()
s.connect(("www.example.com",80))
s.send("GET /hello.txt HTTP/1.1\n\n".encode("utf-8"))
print(s.recv(200).decode())

s.close()

#python3 www_client_socket.py
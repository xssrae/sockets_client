import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "0.0.0.0"
port = 555

try:
    server.bind((ip,port))
    server.listen(5)
    print("Listening in: " +ip+":"+str(port))

    (client_socket,address) = server.accept()
    print("Received from: " + address[0])

    while True:
        data = client_socket.recv(1024)
        print(data)

    server.close()

except NameError as error:
    print("Erro: " + str(error))
    server.close()
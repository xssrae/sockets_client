import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
print("--------TCP CONNECTION TESTER--------\n\n")
target = input("Enter the target's URL or IP: ")
try: #trying a TCP connection with the target
    client.connect((target, 80))
    client.send(b"GET / HTTP/1.1\nHost: \n\n\n")
    recived_packeges = client.recv(1024)

    print(recived_packeges)

except:
    print('\nConection without response..')
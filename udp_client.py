import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("--------UDP CONNECTION TESTER--------\n\n")
target = input("Enter the target's URL or IP: ")

try:
    client.connect("aaaaaaa",(target, 666))
    recived_packeges = client.recvfrom(1024)

    print(recived_packeges)

except:
    print('\nConection without response..')
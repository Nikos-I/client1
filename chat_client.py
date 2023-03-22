# Чат клиент
import socket
import select
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sock_rec():
    while True:
        data_in = server.recv(2048)    
        print (data_in.decode())
        print('\n')
        

IP_address = "192.168.1.101"
Port = 65432

server.connect((IP_address, Port))

rec_thread = threading.Thread(target=sock_rec)
rec_thread.start()

while True:
    message = input("Введите сообщение: ").encode()
    server.send(message)
    print('<Вы> ')
    print(message.decode())
server.close()

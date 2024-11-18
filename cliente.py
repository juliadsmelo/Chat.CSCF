import socket as sock
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                client_socket.close()
                break
        except:
            client_socket.close()
            break

def main():
    HOST = '192.168.15.2'
    PORTA = 6060
    socket_cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket_cliente.connect((HOST, PORTA))

    print(5*"*" + "INICIANDO CHAT" + 5*"*")
    nome = input("Informe seu nome para entrar no chat:\n")
    socket_cliente.sendall(nome.encode())

    thread = threading.Thread(target=receive_messages, args=(socket_cliente,))
    thread.start()

    while True:
        mensagem = input('')
        if mensagem.lower() == 'sair':
            socket_cliente.sendall(mensagem.encode('utf-8'))
            socket_cliente.close()
            break
        else:
            socket_cliente.sendall(mensagem.encode('utf-8'))

if __name__ == "__main__":
    main()

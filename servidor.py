import socket as sock
import threading

clients = []

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def receber_dados(sock_conn, endereco):
    nome = sock_conn.recv(50).decode()
    print(f"Conexão com sucesso com {nome} : {endereco}")
    broadcast(f"{nome} entrou no chat.".encode('utf-8'), sock_conn)
    while True:
        try:
            mensagem = sock_conn.recv(1024).decode()
            if mensagem.lower() == 'sair':
                sock_conn.close()
                clients.remove(sock_conn)
                broadcast(f"{nome} saiu do chat.".encode('utf-8'), sock_conn)
                break
            else:
                print(f"{nome} >> {mensagem}")
                broadcast(f"{nome} >> {mensagem}".encode('utf-8'), sock_conn)
        except:
            sock_conn.close()
            clients.remove(sock_conn)
            broadcast(f"{nome} saiu do chat.".encode('utf-8'), sock_conn)
            break

def main():
    HOST = '192.168.15.2'
    PORTA = 6060
    socket_server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
    socket_server.bind((HOST, PORTA))
    socket_server.listen()
    print(f"O servidor {HOST}:{PORTA} está aguardando conexões...")

    while True:
        sock_conn, ender = socket_server.accept()
        clients.append(sock_conn)
        thread_cliente = threading.Thread(target=receber_dados, args=(sock_conn, ender))
        thread_cliente.start()

if __name__ == "__main__":
    main()

import socket

def start_client(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

    while True:
        word = input("Bitte geben Sie ein Wort ein: ").strip()
        if not word:
            continue
        client.sendall(word.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(response)
        if response.strip() == "Game Over":
            break

    client.close()

if __name__ == "__main__":
    start_client("127.0.0.1", 9999)

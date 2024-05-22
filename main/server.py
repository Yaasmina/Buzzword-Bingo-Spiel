import socket
import threading
from bingocard import Player, log_game_event

def handle_client(client_socket, player, words, log_filename):
    player.generate_bingo_card(words)
    log_game_event(log_filename, f"Spieler {player.id} hat eine Karte erhalten")
    player.display_bingo_card()
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8').strip()
            if not message:
                break
            log_game_event(log_filename, f"Spieler {player.id} wählte: {message}")
            
            if player.mark_bingo_card(message):
                if player.check_winner():
                    log_game_event(log_filename, f"Spieler {player.id} hat gewonnen!")
                    client_socket.sendall(b"Game Over\n")
                    break
                client_socket.sendall(f"Wort {message} markiert\n".encode('utf-8'))
            else:
                client_socket.sendall(f"Wort {message} nicht auf der Karte\n".encode('utf-8'))
        except:
            break
    client_socket.close()

def start_server(ip, port, words):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(2)
    print("Server läuft und wartet auf Verbindungen...")

    log_filename = f"{time.strftime('%Y-%m-%d-%H-%M-%S')}-bingo.log"
    players = []

    while len(players) < 2:
        client_socket, addr = server.accept()
        print(f"Verbindung von {addr} akzeptiert")
        player = Player(len(players) + 1)
        players.append(player)
        threading.Thread(target=handle_client, args=(client_socket, player, words, log_filename)).start()

    server.close()

if __name__ == "__main__":
    words = [
        "Word1", "Word2", "Word3", "Word4", "Word5",
        "Word6", "Word7", "Word8", "Word9", "Word10",
        "Word11", "Word12", "Word13", "Word14", "Word15",
        "Word16", "Word17", "Word18", "Word19", "Word20",
        "Word21", "Word22", "Word23", "Word24", "Word25"
    ]
    start_server("0.0.0.0", 9999, words)
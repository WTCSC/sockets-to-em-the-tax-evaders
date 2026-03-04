import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 5000))
server.listen(1)
print("Waiting for a client...")

client, addr = server.accept()
print(f"Client connected from {addr}")

secret = random.randint(1, 100)
attempts = 0
print(f"Secret number: {secret}")

client.send("I'm thinking of a number between 1 and 100. Guess it!".encode())

while True:
    msg = client.recv(1024).decode()
    if not msg:
        break

    try:
        guess = int(msg)
    except ValueError:
        client.send("Send a valid number!".encode())
        continue

    attempts += 1

    if guess < secret:
        client.send("Too low".encode())
    elif guess > secret:
        client.send("Too high".encode())
    else:
        client.send(f"Correct! You got it in {attempts} attempts!".encode())
        break

client.close()
server.close()

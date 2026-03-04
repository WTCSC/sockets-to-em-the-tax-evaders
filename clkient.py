import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5000))
print("Connected!\n")

welcome = client.recv(1024).decode()
print(f"Server: {welcome}\n")

while True:
    guess = input("Your guess (1-100): ")
    client.send(guess.encode())

    response = client.recv(1024).decode()
    print(f"Server: {response}\n")

    if "Correct" in response:
        break

client.close()

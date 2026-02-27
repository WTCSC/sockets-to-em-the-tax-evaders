# Guess the Number — Socket Game

A simple client-server "Guess the Number" game built with Python's `socket` module.

## What It Does

The **server** picks a random number between 1 and 100. The **client** connects and tries to guess it. After each guess, the server responds with:

- **"Too low!"** — guess a higher number
- **"Too high!"** — guess a lower number
- **"Correct! You got it in X attempt(s)!"** — you win!

## Requirements

- Python 3.6 or higher (uses f-strings)
- No external packages needed — only Python standard library (`socket`, `random`, `sys`)

## How to Run

### 1. Start the Server

Open a terminal and run:

```bash
python3 server.py
```

The server will start listening on port **5000** and wait for a client.

### 2. Start the Client

Open a **second terminal** and run:

```bash
python3 clkient.py
```

The client will connect to `localhost:5000` by default.

### 3. Play!

Type a number between 1 and 100 and press Enter. The server will tell you if your guess is too low, too high, or correct.

### Connecting to a Different Machine

If the server is running on a different computer on your network:

1. Find the server machine's IP address (`hostname -I` on Linux)
2. Open `clkient.py` and change `SERVER_IP` to that IP address:
   ```python
   SERVER_IP = "192.168.1.50"  # Example — use your server's actual IP
   ```
3. Run the client as normal

## Error Handling

The app handles the following network issues:

| Error | What Happens |
|---|---|
| **Port already in use** | Server prints an error and exits cleanly |
| **Connection refused** | Client tells you the server isn't running |
| **Connection timeout** | Client/server detect when the other side stops responding (2 min) |
| **Client disconnects mid-game** | Server detects it and shuts down gracefully |
| **Server crashes mid-game** | Client detects the lost connection and exits |
| **Invalid IP/hostname** | Client prints a clear error message |
| **Ctrl+C interrupt** | Both client and server shut down cleanly |
| **Non-number input** | Server tells client to send a valid number |

## File Structure

```
socjentem/
├── server.py    — The game server (picks number, checks guesses)
├── clkient.py   — The game client (sends guesses, shows hints)
└── README.md    — This file
```

## Example Gameplay

**Server terminal:**
```
[SERVER] Listening on 0.0.0.0:5000...
[SERVER] Waiting for a client to connect...

[SERVER] Client connected from 127.0.0.1:54321
[SERVER] Secret number is 42

[SERVER] Guess #1: 50
[SERVER] Guess #2: 25
[SERVER] Guess #3: 37
[SERVER] Guess #4: 43
[SERVER] Guess #5: 42

[SERVER] Client guessed correctly in 5 attempt(s)!
[SERVER] Closing connections...
[SERVER] Done.
```

**Client terminal:**
```
[CLIENT] Connecting to localhost:5000...
[CLIENT] Connected!

Server: Welcome! I'm thinking of a number between 1 and 100. Take a guess!

Your guess (1-100): 50
Server: Too high! Try again.

Your guess (1-100): 25
Server: Too low! Try again.

Your guess (1-100): 37
Server: Too low! Try again.

Your guess (1-100): 43
Server: Too high! Try again.

Your guess (1-100): 42
Server: Correct! You got it in 5 attempt(s)!

You win! Game over.
[CLIENT] Disconnected.
```

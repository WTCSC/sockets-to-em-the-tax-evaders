# Guess the Number game

A number guessing game made with Python using sockets.

## How It Works

* The server chooses a random number between 1 and 100.
* The client connects and tries to guess the number.
* After each guess, the server replies:
https://github.com/WTCSC/sockets-to-em-the-tax-evaders
  * Too low
  * Too high
  * Correct! (you win)

---

## Requirements

* Python 3.6 or higher


## How to Run

### Step 1: Start the Server

Open a terminal and run:

```bash
python3 server.py
```


---

### Step 2: Start the Client

Open a second terminal and run:

```bash
python3 clkient.py
```

The client connects to `localhost:5000`.

---

### Step 3: Play the Game

Type a number between 1 and 100 and press Enter.
Keep guessing until you get it right!

---

## Playing on Another Computer

If the server is running on a different computer:

1. Find that computer’s IP address.
2. Open `clkient.py`.
3. Change the `SERVER_IP` to the server’s IP address.
4. Run the client again.

---
### Disclaimer
It only shows Lucca Townsend as the contributer because it would not give them access, meaning I had to be the one to commit everything. Stephanie did the README and video, and brody helped me with the code

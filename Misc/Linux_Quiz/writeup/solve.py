from pwn import *

# Replace with the actual address and port if different
HOST = "localhost"
PORT = 13337

# Establish a remote connection
conn = remote(HOST, PORT)

# Receive the welcome message
print(conn.recvline().decode())

# Store the questions and answers for easy reference
QUESTIONS = {
    "What is the command to list all files in a directory?": "A",
    "What is the command to change directory?": "C",
    "What is the command to list all running auxiliary processes?": "A",
    "What is the command to change to the root user of the system?": "B",
    "What is the correct path in which DNS Name resolutions are stored?": "B",
    "What is the command to show the current working directory?": "A",
    "What command is used to display the first lines of a file?": "C",
    "What is the command to find files in a directory hierarchy?": "B",
    "What is thecommand to display disk usage?": "A",
    "What command shows the manual page of a command?": "A"
}

# Iterate through the quiz questions
for question in QUESTIONS:
    print(conn.recvuntil(b"Your answer (A, B, C, D): ").decode())  # Receive question and choices
    answer = QUESTIONS[question].encode() 
    conn.sendline(answer)  # Send the answer 
    print(conn.recvline().decode())  # Receive feedback ("Correct!" or "Incorrect...")

# Receive the flag
flag = conn.recvline().decode()
print(flag)

conn.close()
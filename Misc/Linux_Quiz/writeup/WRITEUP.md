# Linux Quiz
**Description:** Can you pass the Linux Quiz to receive the flag?

## Solution
**Explanation**

1. **pwntools Import:** We import the necessary `remote` function from the `pwn` library.

2. **Connection:** We establish a remote connection to the specified `HOST` and `PORT` where the quiz server is running.

3. **Welcome Message:** We receive and print the initial welcome message.

4. **QUESTIONS Dictionary:** This dictionary conveniently stores the correct answers, so you don't have to type them manually each time.

5. **Quiz Loop:**
   - We iterate through each question in the `QUESTIONS` dictionary.
   - `conn.recvuntil()` is used to receive the question text and answer choices.
   - The script looks up the correct answer from the `QUESTIONS` dictionary and sends it using `conn.sendline()`.
   - Feedback from the server ("Correct!" or "Incorrect...") is received and printed.

6. **Flag Acquisition:** The script captures the flag in the server's response and displays it. 

**How to Run**

1. Make sure you have pwntools installed: `pip install pwntools`
2. Save the code as `solve.py`
3. Start your quiz server in another terminal.
4. Run the script: `python solve.py`
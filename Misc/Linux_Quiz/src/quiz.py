import socketserver
import threading
import logging
# Additional questions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
QUESTIONS = {
    "What is the command to list all files in a directory?": ["A. ls", "B. dir", "C. cd", "D. tree", "A"],
    "What is the command to change directory?": ["A. ls", "B. dir", "C. cd", "D. tree", "C"],
    "What is the command to list all running auxiliary processes?": ["A. ps aux", "B. kill", "C. top", "D. killall", "A"],
    "What is the command to change to the root user of the system?": ["A. sudo", "B. su -", "C. root", "D. sudo su", "B"],
    "What is the correct path in which DNS Name resolutions are stored?": ["A. /etc/hosts", "B. /etc/resolv.conf", "C. /etc/hostname", "D. /etc/hosts.conf", "B"],
    "What is the command to show the current working directory?": ["A. pwd", "B. cd", "C. ls", "D. dir", "A"],
    "What command is used to display the first lines of a file?": ["A. tail", "B. less", "C. head", "D. cat", "C"],
    "What is the command to find files in a directory hierarchy?": ["A. grep", "B. find", "C. locate", "D. ls", "B"],
    "What is the command to display disk usage?": ["A. df", "B. du", "C. diskfree", "D. diskusage", "A"],
    "What command shows the manual page of a command?": ["A. man", "B. help", "C. info", "D. cmd", "A"]
}

FLAG = "GrizzCTF{n0w_y04_kn0w_4_l1l_l1nux_3h}"

class QuizHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall("Welcome to the Linux CLI Quiz!\n".encode())
        correct_answers = 0
        for question, choices in QUESTIONS.items():
            self.request.sendall(f"\n{question}\n".encode())
            for choice in choices[:-1]:
                self.request.sendall(f"{choice}\n".encode())
            self.request.sendall("Your answer (A, B, C, D): ".encode())
            answer = self.request.recv(1024).strip().upper()
            if answer == choices[-1].encode():
                correct_answers += 1
                self.request.sendall("Correct!\n".encode())
            else:
                self.request.sendall("Incorrect. Try again next time!\n".encode())
                return
        if correct_answers == len(QUESTIONS):
            self.request.sendall(f"Congratulations! Here's your flag: {FLAG}\n".encode())

class ThreadedQuizServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    HOST, PORT = "localhost", 13337

    with ThreadedQuizServer((HOST, PORT), QuizHandler) as server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()
        print(f"Server started at {HOST}:{PORT}")

        try:
            server_thread.join()
        except KeyboardInterrupt:
            server.shutdown()
            server.server_close()
            print("Server stopped.")

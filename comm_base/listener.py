import socket
import subprocess

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# listen on all interfaces to find docker interface
srvaddr = ('0.0.0.0', 8888)
run_cmd = "/./open.sh"

sock.bind(srvaddr)
sock.listen(1)
while 1:
    conn, client_addr = sock.accept()
    data = conn.recv(8)
    
    stringdata = data.decode('utf-8')
    
    if stringdata == "run\n":
        p = subprocess.Popen(run_cmd.split(), stdout=subprocess.PIPE)
    conn.close()

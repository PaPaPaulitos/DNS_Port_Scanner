import threading
import socket
from controller.search_dns import Search_DNS



def portas():
        portas = 65534
        for num in range(portas):
            yield num

def scan_ip(ip,porta):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, porta))
        sock.close()
        if result == 0:
            print(f"{ip}:{porta}")

host = input("Alvo: ")
threads = list()

search_dns = Search_DNS(host)

for ip in search_dns.search_dns():
    print(f"Agora testando o IP {ip}")
    for porta in portas():
        thread = threading.Thread(target=scan_ip ,args=(ip,porta))
        threads.append(thread)
        thread.start()


for thread in threads:
    thread.join()   
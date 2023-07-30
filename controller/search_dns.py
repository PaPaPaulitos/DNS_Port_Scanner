import socket


class Search_DNS:
    def __init__(self,host) -> None:
        self.__brute = ['ns1','ns2','ns3','ns4','www','ftp','intranet','mail']
        self.__host = host

    def search_dns(self):
        ips = list()

        with open(r".\bruteforce.txt",'r') as arq:
            bruteforce = arq.readlines()
        
        for nome in bruteforce:
            DNS = nome.strip("\n") + "." + self.__host
            try:
                print(f'{DNS}: {socket.gethostbyname(DNS)}')
                ips.append(socket.gethostbyname(DNS))
            except socket.gaierror:
                pass
            
        return ips

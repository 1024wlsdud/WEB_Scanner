import asyncio
import nmap
import save_result

def scaning(ip,port,options=''):
    nm = nmap.PortScanner()    
    return(nm.scan(ip,port))

from port_scan import *
from read_setting import *
import ipaddress
from netaddr import iter_iprange
import asyncio
import time

set_json = read_setting("test.json")
ip_range = set_json['ip_range'].replace(" ","").split('-')
generator = iter_iprange(ip_range[0], ip_range[1], step=1)

def main():
    for ip in generator :
        result = scaning(str(ip), set_json['port_range'])
        print(result)
    # futures = [asyncio.ensure_future(scaning(str(ip),set_json['port_range'])) for ip in generator]
    # result = await asyncio.gather(*futures)

main()  

# print(f"started at {time.strftime('%X')}")
# asyncio.run(main())
# print(f"finish at {time.strftime('%X')}")    

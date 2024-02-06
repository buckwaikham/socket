#!/usr/bin/env python3

import os

ip_list = ['8.8.8.8' '8.8.4.4' '1.1.1.1' '4.4.4.4']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful, Host is UP!")
    else:
        print(f"DOWN {ip} Ping Unsuccessful, Host is DOWN.")

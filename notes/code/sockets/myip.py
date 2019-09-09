import netifaces as ni
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
print(ip)

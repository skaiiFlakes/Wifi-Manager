import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures

os.system('cls')
s_proxies = []
path = r"path" #add path to csv file

def getProxies_by_online():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    o_proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            o_proxies.append(proxy)
        else:
            pass
    return o_proxies

def getProxies_by_file():
    file = open(path, "r+")
    lines = file.readlines()
    f_proxies = []
    for line in lines:
        f_proxies.append(line)
    return f_proxies

def check(proxy):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get('https://httpbin.org/ip', headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=1)
        status = r.status_code
        if status == 200:
            # print(r.json(), proxy, "successful")
            s_proxies.append(proxy)
    except:
        # print(proxy)
        pass
    return proxy

proxylist = []

f_proxies = getProxies_by_file()
for proxy in f_proxies:
    proxylist.append(proxy.strip().replace("\n",""))

o_proxies = getProxies_by_online()
for proxy in f_proxies:
    proxylist.append(proxy.strip().replace("\n",""))

print(proxylist)

print(f"Proxies retrieved: {len(proxylist)}\n")

with concurrent.futures.ThreadPoolExecutor() as executor:
        print("Testing proxies...\n")
        executor.map(check, proxylist)

if len(s_proxies) > 0:
    print("Working proxies:")
    for i in s_proxies:
        print(i)
else:
    print("No working proxies found")

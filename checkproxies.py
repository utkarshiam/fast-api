import threading
import queue
import requests

q= queue.Queue()
valid_proxies = []

with open("proxies.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)
        
def checkProxies():
    global q
    while not q.empty():
        proxy = q.get()
        print("proxy", proxy)
        try: 
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy})
        except: 
            continue
        
        if res.status_code == 200:
            print("proxy works =====>", proxy)
            
for _ in range(10):
    threading.Thread(target=checkProxies).start()
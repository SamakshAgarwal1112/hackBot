import requests as req
import random

def set_working(proxy):
	working.add(proxy) 
	not_working.discard(proxy) 
 
def set_not_working(proxy):
	working.discard(proxy) 
	not_working.add(proxy)

proxies_list = ["103.168.155.116:80", "41.77.188.131:80", "62.210.114.201:8080", "154.208.10.126:80", "74.48.7.43:80"]
working = set(proxies_list) 
not_working = set() 

session = req.Session()

VALID_STATUSES = [200, 301, 302, 307, 404]
 
def get_data(url):
	proxy = get_random_proxy()

	try: 
		response = session.get(url, proxies={'http': f"http://{proxy}"}, timeout=30,headers=headers) 
		if response.status_code in VALID_STATUSES: 
			set_working(proxy) 
		else: 
			set_not_working(proxy) 
 
		return response 
	except Exception as e: 
		set_not_working(proxy) 
  
def get_random_proxy():
	available_proxies = list(working)
	if not available_proxies: 
		raise Exception("no proxies available") 
	return random.choice(available_proxies)

user_agent_list = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
 	'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15', 
]
    
headers = {'User-Agent': random.choice(user_agent_list),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Language': 'en-US,en;q=0.9',
'Accept-Encoding': 'gzip, deflate, br'}
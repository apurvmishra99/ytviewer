import re
import requests
from os import _exit
from time import sleep
from random import choice,uniform
from argparse import ArgumentParser
from threading import Thread
from traceback import print_exc
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,ProxyType

parser=ArgumentParser()
parser.add_argument('-t','--threads',type=int,help='number of threads',default=15)
parser.add_argument('-u','--url',help='video url',default='',required=True)
parser.add_argument('-d','--duration',help='duration of video in seconds',default=5*60)
parser.add_argument('-p','--proxies',help='proxies list')
args=parser.parse_args()

def bot(url):
	try:
		while True:
			proxy.http_proxy=choice(proxies)
			proxy.ssl_proxy=proxy.http_proxy
			print(proxy.http_proxy)
			chrome_options.add_argument('user-agent="{}"'.format(agent.random))
			capabilities=webdriver.DesiredCapabilities.CHROME
			proxy.add_to_capabilities(capabilities)
			driver=webdriver.Chrome(options=chrome_options,desired_capabilities=capabilities)
			driver.get(args.url)
			sleep(float(args.duration))
			driver.close()
	except KeyboardInterrupt:_exit(0)
	except Exception:
		print_exc()
		_exit(1)

try:
	if args.proxies:
		proxies=open(args.proxies,'r').read().split('\n')
	else:
		proxies=re.findall(re.compile('<td>([\d.]+)</td>'),str(requests.get('https://free-proxy-list.net/').content))
		proxies=['%s:%s'%x for x in list(zip(proxies[0::2],proxies[1::2]))]
	print('%d proxies successfully loaded!'%len(proxies))
	proxy=Proxy()
	proxy.proxy_type=ProxyType.MANUAL
	agent=UserAgent()
	chrome_options=webdriver.ChromeOptions()
	chrome_options.add_argument('--mute-audio')
	for i in range(args.threads):
		t=Thread(target=bot,args=(args.url,))
		t.deamon=True
		t.start()
		sleep(uniform(2.0,4.0))
except KeyboardInterrupt:_exit(0)
except Exception:
	print_exc()
	_exit(1)
import re
import requests
from os import _exit,path
from time import sleep
from random import choice,uniform
from argparse import ArgumentParser
from threading import Thread
from traceback import print_exc
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy,ProxyType

parser=ArgumentParser()
parser.add_argument('-t','--threads',type=int,help='set number of the threads',default=15)
parser.add_argument('-u','--url',help='set url of the video/set the path of the urls list',default='',required=True)
parser.add_argument('-d','--duration',help='set the duration of the video in seconds',type=float)
parser.add_argument('-p','--proxies',help='set the path of the proxies list')
parser.add_argument('-us','--user-agent',help='set the user agent for the driver/set the path of the user agents list for the driver')
parser.add_argument('-dr','--driver',help='set the driver for the bot',choices=['chrome','firefox'],default='chrome')
args=parser.parse_args()

def bot(url):
	try:
		while True:
			url=choice(urls)
			proxy.http_proxy=choice(proxies)
			proxy.ssl_proxy=proxy.http_proxy
			print(proxy.http_proxy)
			user_agent=choice(user_agents) if args.user_agent else user_agents.random
			if args.driver=='chrome':
				chrome_options=webdriver.ChromeOptions()
				chrome_options.add_argument('user-agent="{}"'.format(user_agent))
				capabilities=webdriver.DesiredCapabilities.CHROME
				proxy.add_to_capabilities(capabilities)
				driver=webdriver.Chrome(options=chrome_options,desired_capabilities=capabilities)
			else:
				firefox_profile=webdriver.FirefoxProfile()
				firefox_profile.set_preference('general.useragent.override',user_agent)
				firefox_profile.set_preference('network.proxy.type',1)
				firefox_profile.set_preference('network.proxy.http',proxy.http_proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.http_port',proxy.http_proxy.split(':')[1])
				firefox_profile.set_preference('network.proxy.ssl',proxy.ssl_proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.ssl_port',proxy.ssl_proxy.split(':')[1])
				firefox_profile.update_preferences() 
				driver=webdriver.Firefox(firefox_profile=firefox_profile)
			driver.set_page_load_timeout(120);
			try:
				driver.get(url)
				if not any(x in driver.page_source for x in ['ERR_PROXY_CONNECTION_FAILED','ERR_CONNECTION_TIMED_OUT']):
					player=None
					while player is None:
						player=driver.execute_script("return document.getElementById('movie_player');")
					driver.execute_script("arguments[0].setVolume(0);",player)
					sleep(args.duration or float(driver.execute_script("return arguments[0].getDuration()",player)+uniform(1.0,5.0)))
			except TimeoutException:pass
			driver.close()
	except KeyboardInterrupt:_exit(0)
	except Exception:
		print_exc()
		_exit(1)

try:
	if args.url:
		if path.isfile(args.url):
			urls=list(filter(None,open(args.url,'r').read().split('\n')))
		else:
			urls=[args.url]
	if args.proxies:
		proxies=open(args.proxies,'r').read().split('\n')
	else:
		proxies=re.findall(re.compile('<td>([\d.]+)</td>'),str(requests.get('https://www.sslproxies.org/').content))
		proxies=['%s:%s'%x for x in list(zip(proxies[0::2],proxies[1::2]))]
	print('%d proxies successfully loaded!'%len(proxies))
	proxy=Proxy()
	proxy.proxy_type=ProxyType.MANUAL
	if args.user_agent:
		if path.isfile(args.user_agent):
			user_agents=list(filter(None,open(args.user_agent,'r').read().split('\n')))
		else:
			user_agents=[args.user_agent]
	else:
		user_agents=UserAgent()
	for i in range(args.threads):
		t=Thread(target=bot,args=(args.url,))
		t.deamon=True
		t.start()
		sleep(uniform(2.0,4.0))
except KeyboardInterrupt:_exit(0)
except Exception:
	print_exc()
	_exit(1)
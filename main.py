import re
import requests
from os import _exit,path
from sys import stdin
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
parser.add_argument('-hd','--headless',help='set the driver as headless',action='store_true')
args=parser.parse_args()

def exit(exit_code):
	if exit_code!=0:
		print_exc()
	_exit(exit_code)
def bot():
	try:
		while True:
			url=choice(urls)
			proxy=choice(proxies)
			print(proxy)
			user_agent=choice(user_agents) if args.user_agent else user_agents.random
			if args.driver=='chrome':
				chrome_options=webdriver.ChromeOptions()
				chrome_options.add_argument('--proxy-server={}'.format(proxy))
				chrome_options.add_argument('user-agent="{}"'.format(user_agent))
				if args.headless:
					chrome_options.add_argument('--headless')
				driver=webdriver.Chrome(options=chrome_options)
			else:
				options=webdriver.FirefoxOptions()
				options.headless=args.headless
				firefox_profile=webdriver.FirefoxProfile()
				firefox_profile.set_preference('general.useragent.override',user_agent)
				firefox_profile.set_preference('network.proxy.type',1)
				firefox_profile.set_preference('network.proxy.http',proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.http_port',proxy.split(':')[1])
				firefox_profile.set_preference('network.proxy.ssl',proxy.split(':')[0])
				firefox_profile.set_preference('network.proxy.ssl_port',proxy.split(':')[1])
				firefox_profile.update_preferences()
				driver=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
			driver.set_page_load_timeout(120);
			try:
				driver.get(url)
				if not 'ERR_' in driver.page_source:
					player=None
					while player is None:
						player=driver.execute_script("return document.getElementById('movie_player');")
					driver.execute_script("arguments[0].setVolume(0);",player)
					sleep(args.duration or float(driver.execute_script("return arguments[0].getDuration()",player)+uniform(1.0,5.0)))
			except TimeoutException:pass
			driver.quit()
	except KeyboardInterrupt:exit(0)
	except:exit(1)

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
	if args.user_agent:
		if path.isfile(args.user_agent):
			user_agents=list(filter(None,open(args.user_agent,'r').read().split('\n')))
		else:
			user_agents=[args.user_agent]
	else:
		user_agents=UserAgent()
	for i in range(args.threads):
		t=Thread(target=bot)
		t.daemon=True
		t.start()
		sleep(uniform(2.0,4.0))
	stdin.read(1)
	exit(0)
except KeyboardInterrupt:exit(0)
except:exit(1)

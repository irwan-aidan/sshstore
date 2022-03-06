import os
import sys
import urllib
from urllib2 import Request, urlopen
from HTMLParser import HTMLParser
from datetime import datetime

line_1 = 'sshstores[?]># '
line_u = '$input_username[?]-># '
line_p = '$input_password[?]-># '
class sshstores(HTMLParser):
    def handle_data(self, data):
		if 'Sorry server accounts limit exceeded, please choose another server' in data: print("[!] Sorry server accounts limit exceeded, please choose another server")
		elif 'You account was successfully created.' in data: print("[+] Success! You account was successfully created.")
		elif '.sshstores.vip /' in data: print('[+] %s' % data)
		elif '.sshstores.net /' in data: print('[+] %s' % data)
		elif user in data: print('[+] Username:%s' % data)
		elif pw in data: print('[+] Password:%s' % data)
		elif '143,' in data: print('[+] Dropbear Port:%s' % data)
		elif '997' in data: print('[+] OpenSSH Port:%s' % data)
		elif '7300,' in data: print('[+] UDPGW Port:%s' % data)	
		elif '443' in data: print('[+] SSL/TLS Port:%s' % data)	
		elif '80,' in data: print('[+] Squid Port:%s' % data)
		elif 'Created date' in data:print('[+] Created date: %s' % d)
		elif ' 2020' in data: print('[+] Expired date:%s' % data)
def host(server):
	if server == '1' : return "http://vip.sshstores.net/create-account-server-ssl3-1/Singapore"
	if server == '2' : return "http://vip.sshstores.net/create-account-server-ssl3-2/Singapore"
	if server == '3' : return "http://vip.sshstores.net/create-account-server-ssl3-3/Singapore"
	if server == '4' : return "http://vip.sshstores.net/create-account-server-ssl3-4/Singapore"
	if server == '5' : return "http://vip.sshstores.net/create-account-server-ssl3-5/Singapore"
	if server == '6' : return "http://vip.sshstores.net/create-account-server-ssl3-6/Singapore"
	if server == '7' : return "http://vip.sshstores.net/create-account-server-ssl7-1/Singapore"
	if server == '8' : return "http://vip.sshstores.net/create-account-server-ssl7-2/Singapore"
	if server == '9' : return "http://vip.sshstores.net/create-account-server-ssl7-3/Singapore"
	if server == '10' : return "http://vip.sshstores.net/create-account-server-ssl7-4/Singapore"
	if server == '11' : return "http://vip.sshstores.net/create-account-server-ssl7-5/Singapore"
	if server == '12' : return "http://vip.sshstores.net/create-account-server-ssl7-6/Singapore"
	if server == '13' : return "http://vip.sshstores.net/create-account-server-ssl30-1/Singapore"
	if server == '14' : return "http://vip.sshstores.net/create-account-server-ssl30-2/Singapore"
	if server == '15' : return "http://sshstores.net/create-account-server-sgdo-1/Singapore"
	if server == '16' : return "http://sshstores.net/create-account-server-sgdo-2/Singapore"
	if server == '17' : return "http://sshstores.net/create-account-server-sgdo-3/Singapore"
	
def createaccount(server, username, password):
	url = host(server)
	user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
	values = {'username': username,
			  'password': password,
			  'code': '12345',
			  'inputcode': '12345',
			  'submit': 'create'}
	headers = {'User-Agent': user_agent}

	data = urllib.urlencode(values)
	req = Request(url, data, headers)
	response = urlopen(req)
	the_page = response.read()
	parser = sshstores()
	parser.feed(the_page)	
	
def inputuser(server):
	global now
	global d, exp
	now = datetime.now() 
	d = now.strftime("%d %b %Y")
	global user
	global pw
	user = raw_input(line_u)
	pw = raw_input(line_p)
	createaccount(server, user, pw)
	
def menu():	
	print('1. VIP Singapore SSL 3-1 3 days')
	print('2. VIP Singapore SSL 3-2 3 days')
	print('3. VIP Singapore SSL 3-3 3 days')
	print('4. VIP Singapore SSL 3-4 3 days')
	print('5. VIP Singapore SSL 3-5 3 days')
	print('6. VIP Singapore SSL 3-6 3 days')
	print('7. VIP Singapore SSL 7-1 7 days')
	print('8. VIP Singapore SSL 7-2 7 days')
	print('9. VIP Singapore SSL 7-3 7 days')
	print('10. VIP Singapore SSL 7-4 7 days')
	print('11. VIP Singapore SSL 7-5 7 days')
	print('12. VIP Singapore SSL 7-6 7 days')
	print('13. VIP Singapore SSL 30-1 30 days')
	print('14. VIP Singapore SSL 30-2 30 days')
	print('15. Singapore DO 1 3 days')
	print('16. Singapore DO 2 3 days')
	print('17. Singapore DO 3 3 days')
	server = raw_input(line_1)
	if server == '1':inputuser('1')
	elif server == '2':inputuser('2')
	elif server == '3':inputuser('3')
	elif server == '4':inputuser('4')
	elif server == '5':inputuser('5')
	elif server == '6':inputuser('6')
	elif server == '7':inputuser('7')
	elif server == '8':inputuser('8')
	elif server == '9':inputuser('9')
	elif server == '10':inputuser('10')
	elif server == '11':inputuser('11')
	elif server == '12':inputuser('12')
	elif server == '13':inputuser('13')
	elif server == '14':inputuser('14')
	elif server == '15':inputuser('15')
	elif server == '16':inputuser('16')
	elif server == '17':inputuser('17')
	
if __name__ == "__main__":
	menu()

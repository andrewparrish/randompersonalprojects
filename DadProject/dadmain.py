#stuff	
from BeautifulSoup import BeautifulSoup as BS
import urllib2

class Realtor:
	def __init__(self, name, phone, address, email):
			self.name = name
			self.phone = phone
			self.address = address
			self.email = email


i = 1
allhtml = []
while (i <= 30)
	html = urllib2.urlopen('http://www.albanyboardofrealtors.com/default.asp?content=agents&menu_id=235349&agt_off_option=last_name&page='+i)
	soup = BS(html)
	allhtml.append(soup)
	i+=1

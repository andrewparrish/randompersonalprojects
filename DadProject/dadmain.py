#stuff	
from BeautifulSoup import BeautifulSoup as BS
import urllib2

class Realtor:
	def __init__(self, name, phone, address, email):
			self.name = name
			self.phone = phone
			self.address = address
			self.email = email


#albany realty site
def albany():
	i = 1
	allhtml = []
	while (i <= 2):
		html = urllib2.urlopen('http://www.albanyboardofrealtors.com/default.asp?content=agents&menu_id=235349&agt_off_option=last_name&page='+str(i))
		soup = BS(html)
		matches = soup.findAll('td')
		for match in matches:
			print match
			print "########################################"
			if 'agent_heading_inline' in match:
				allhtml.append(match)
		i+=1
	return allhtml

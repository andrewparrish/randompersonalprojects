#stuff	
from BeautifulSoup import BeautifulSoup as BS
import urllib2

class Realtor:
	def __init__(self, name, title, phone, street, city, zipcode, state, email):
			self.name = name
			self.title = title
			self.phone = phone
			self.street = street
			self.city = city
			self.zipcode = zipcode
			self.state = state
			self.email = email


#albany realty site
def albany():
	i = 1
	allhtml = []
	realtors = []
	while (i <= 2):
		html = urllib2.urlopen('http://www.albanyboardofrealtors.com/default.asp?content=agents&menu_id=235349&agt_off_option=last_name&page='+str(i))
		soup = BS(html)
		matches = soup.findAll('td')
		for match in matches:
			if 'agent_heading_inline' in str(match):
				allhtml.append(match)
		i+=1
	for tag in allhtml:
		namegrab = tag.findAll('div', {'class' : 'agent_heading_inline'})
		name = namegrab[0].getText()
		info = tag.findAll('div', {'class' : 'agent_info_inline'})
	

	return allhtml	

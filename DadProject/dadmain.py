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
		fullname = namegrab[0].getText()
		fullname = fullname.split()
		name = fullname[0]+' '+fullname[1]
		if 'Broker' in fullname:
			title = 'Broker'
		else:
			title = ''
		info = tag.findAll('div', {'class' : 'agent_info_inline'})
		uneditedphone = info[0].getText()
		broken = uneditedphone.split()
		cutzip = broken[1].replace(')', '')
		phone = cutzip+broken[2].replace('-', '')
		phone = phone.replace('(', '')
		if info[1].getText() is '' or info[1].getText() is None:
			street = info[1].getText()
		else:
			street = info[1].getText()+' '+info[2].getText()
		#email = info[3].getText()
		if len(info) is 3:
			print info
		span = tag.findAll('span')
		city = span[0].getText()
		state = span[1].getText()
		zipcode = span[2].getText()
		#realtor = Realtor(name, title, phone, street, city, zipcode, state, email)
		#realtors.append(realtor)
	return realtors	

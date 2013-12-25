#stuff	
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import re
import csv

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


#converting realtors array to csv file
def csvrealtors(realtors):
	csvfile = open('realtors.csv', 'wb')
	writer = csv.writer(csvfile, delimiter=',')
	writer.writerow(['Name', 'Title', 'Phone', 'Street', 'City', 'Zipcode', 'State', 'Email'])
	for realtor in realtors:
		writer.writerow([realtor.name, realtor.title, realtor.phone, realtor.street, realtor.city, realtor.zipcode, realtor.state, realtor.email])

#albany realty site
def albany():
	i = 1
	allhtml = []
	realtors = []
	while (i <= 30):
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
		infos = tag.findAll('div', {'class' : 'agent_info_inline'})
		
		#Necessary inputs
		phone = ''
		street = ''
		zipcode = ''
		city = ''
		state = ''
		email = ''
		
		for info in infos:
			text = info.getText()
			phoneregexp = re.compile('\(\d+\)')
			addressregexp = re.compile('^\d+\s+\D+')
			emailregexp = re.compile('\w+@\w+.\D+')
			poboxregexp = re.compile('PO Box\s+\d+')

			if phoneregexp.search(text) is not None:
				if 'C' in text:
					phone = text
				else:
					if phone is '':
						phone = text
			elif addressregexp.search(text) is not None:
				street = text
			elif poboxregexp.search(text) is not None:
				street = text
			elif emailregexp.search(text) is not None:
				email = text
			elif 'span' in str(info):
				spans = tag.findAll('span')
				city = spans[0].getText()
				state = spans[1].getText()
				zipcode = spans[2].getText()					
		realtor = Realtor(name, title, phone, street, city, zipcode, state, email)
		realtors.append(realtor)
	return realtors	

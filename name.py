import sys
import requests as r
from lxml import html
"""
			Stage 1
	----------------------------------------------------------------------------------
	Check If The User Has Input The Name Or Not
	"""

if len(sys.argv) < 2:
	print "Usage : python name.py Name_to_Search"
	sys.exit()

"""	
			Stage 2
	-----------------------------------------------------------------------------------
	Open Bachpan.com for Hindu Name and get its html

	"""

page = r.get("http://www.bachpan.com/Meaning-of-%s.aspx" % str(sys.argv[1]))

tree = html.fromstring(page.text)

"""
			Stage 3
	------------------------------------------------------------------------------------
	Search The Html Document Using lxml's Xpath And If name is Found, Print its Meaning
	
	"""

name = tree.xpath(".//*[@id='ctl00_ctl00_cntRightContent_cntRightContent_lblName']/text()")
if (name) :

	meaning = tree.xpath(".//*[@id='ctl00_ctl00_cntRightContent_cntRightContent_lblMeaning']")

	gender = tree.xpath(".//*[@id='ctl00_ctl00_cntRightContent_cntRightContent_lblGender']/text()")		

	religion = tree.xpath(".//*[@id='ctl00_ctl00_cntRightContent_cntRightContent_lblReligion']/text()")


	print "\tName:\t\t", name #[i.text_content() for i in name]
	print "\tMeaning:\t", [i.text_content() for i in meaning] 
	print "\tGender:\t\t",gender#[i.text_content() for i in gender] 
	print "\tReligion:\t",religion #[i.text_content() for i in religion] 
	""" 
			Stage 4
	----------------------------------------------------------------------------------------
	If Name Not Found Then Open Babynames.com and Search On that Site For Name
	
	"""

else :
	page = r.get("http://www.babynames.com/name/%s" % str(sys.argv[1]))
	tree = html.fromstring(page.text)

	name = tree.xpath(".//*[@id='contentframe2']/div[6]/div[1]/text()")
	meaning = tree.xpath(".//*[@id='contentframe2']/div[6]/div[2]/text()")
	origin = tree.xpath(".//*[@id='contentframe2']/div[6]/div[3]/text()")

	if name:
		print "\t\t", name
		print "\tMeaning:\t" ,meaning
		print "\tOrigin:\t\t" ,origin

	#If Name Not Found Print Name Is Not Found	
	else:
		print "\n\t\tSorry your name not found !\n"	
import requests 
import re
from utils import stripHtml
from bs4 import BeautifulSoup
from utils import write_to_csv
import simplejson
import couchdb
import traceback

#establish the connection with couchdb server 
couch = couchdb.Server()

#Use the existing DB - Flipkart
db=couch['flipkart']

#get the html source of a given url 
def get_html_source(url):
	r = requests.get(url)
	return r.text

#given a soup object, it will return authorname, title , data and posted_date in a dictionary format 
def getReviewData(review):
	a = {} 
	try:
		a['author_name'] = review.find('span',attrs = {'class':re.compile('.*review-username')}).renderContents()
	except:
		try:
			a['author_name'] = stripHtml(review.find('a',attrs={'href':re.compile('.*user\-profiles.*')}).renderContents())
		except:
			a['author_name'] = ''
	a['data'] = stripHtml(review.find('span',attrs = {'class':'review-text'}).renderContents())
	a['title'] = stripHtml(review.find('strong').renderContents())
	try:
		a['posted_date'] = stripHtml(review.find('div',attrs={'class':'date line fk-font-small'}).renderContents())
	except:
		a['posted_date'] = 'NA'
	return a

#Saving the list of dictionary to couchdb 
def saveToCouchDB(data):
	for result in data:
		db.save(result)

#Save the result to multiple datasink
def save(result):
	write_to_csv(result,'/home/soundarya/test.csv')
	simplejson.dump(result,open('/home/soundarya/test.dmp','w'))
	saveToCouchDB(result)

#Result contains the list of dictionaries 
def getReviewsForSinglePage(soup):
	result = []
	reviews = soup.findAll('div',attrs = {'class':'fclear fk-review fk-position-relative line '})
	print len(reviews)
	for review in reviews:
		try:
			t = getReviewData(review)
			result.append(t)
		except:
			pass
	return result

#given a url, will give the soup object 
def getSoup(url):
	print "Getting Soup this url : %s"%url
	html_doc = get_html_source(url)	
	soup = BeautifulSoup(html_doc,'html.parser')
	return soup

#main function 
if __name__ == "__main__":	
	url = "http://www.flipkart.com/apple-iphone-6/product-reviews/ITME8DVFEUXXBM4R?pid=MOBEYGPZAHZQMCKZ&sort=most_recent"
	while True:		
		try:
			soup = getSoup(url)
			my_results = getReviewsForSinglePage(soup)	
			save(my_results)
			#next_page = soup.find('a',attrs = {'class':'nav_bar_next_prev'})
			next_page = soup.find('big',text=u'\u203a').findParent('a')
			url = 'http://www.flipkart.com' + next_page['href']
			print "Next page is %s"%url
		except:
			# print traceback.print_exc()
			print 'Fetched all pages'
			print 'stopped'
			break
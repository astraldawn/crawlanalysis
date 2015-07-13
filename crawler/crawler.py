import re
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
print "----- Doing the login -----"
br.open("https://myaccount.nytimes.com/auth/login")
print br.title()
br.select_form(nr=0)
br.form['userid'] = "markleechuyong@gmail.com"
br.form['password'] = "musicshare"
br.submit()
print "----- Login success -----"
print br.title()
br.open("http://query.nytimes.com/search/sitesearch/#/*/from20140101to20150101/document_type%3A%22article%22/1/allauthors/relevance/World/")
print "----- Navigating to first page of archives -----"
print br.title()

print br.response().read()
soup = BeautifulSoup(br.response(),"html5lib")
 
body_tag = soup.body
resultsdiv = soup.find('div', id="searchResults")


print resultsdiv.prettify()

#print soup.prettify()
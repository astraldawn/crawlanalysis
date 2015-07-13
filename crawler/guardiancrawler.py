import mechanize
from bs4 import BeautifulSoup
import re

# http://content.guardianapis.com/search?api-key=test&show-tags=all&from-date=2014-01-01&to-date=2015-01-01
# Full list of sections: http://content.guardianapis.com/sections?api-key=gch6nzm2k8kfckzf3c8mtefy
# http://content.guardianapis.com/search?api-key=gch6nzm2k8kfckzf3c8mtefy&show-tags=all&page=1&order-by=newest&section=world|uk-news|us-news&from-date=2014-01-01&to-date=2015-01-01
# 16000 articles

br = mechanize.Browser()
br.open("http://www.theguardian.com/uk-news/davehillblog/2015/jan/01/mount-pleasants-sombre-lessons-for-london-in-2015")
print br.title()
soup = BeautifulSoup(br.response(),"html5lib")
# print soup.prettify()
mydivs = soup.findAll("div", class_="content__article-body from-content-api js-article__body")
for div in mydivs:
    for j in div:
        outputstr = re.sub('<[^>]*>', '', str(j))
        print outputstr
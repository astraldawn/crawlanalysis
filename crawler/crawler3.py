import urllib2
import json
import mechanize
from time import sleep

opening = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name%3A%28%22World%22%29"
startdate = "begin_date=20140101"
enddate = "end_date=20150101"
page = "page="
key = "api-key=57a53bc0e5186e9d1ae82fbeed6b3238:7:72493178"

# br = mechanize.Browser()
# print "----- Doing the login -----"
# br.open("https://myaccount.nytimes.com/auth/login")
# print br.title()
# br.select_form(nr=0)
# br.form['userid'] = "markleechuyong@gmail.com"
# br.form['password'] = "musicshare"
# br.submit()
# print "----- Login success -----"

pagestart = 0

print "----- Begin the crawl -----"
for i in range(pagestart, 10):
    querysrc = [opening, startdate, enddate, page+str(i), key]
    query = "&".join(querysrc)
    print "----- " + query + " -----"
    jstrs = urllib2.urlopen(query).read()
    t = jstrs.strip('()')
    tss= json.loads( t )  # error no joson object
    print "PAGE: " + str(i) + "   started from " + str(pagestart)
    for item in tss['response']['docs']:
        # print item['web_url']
        print "Headline: " + item['headline']['main']
        print "Content: " + item['lead_paragraph']
        print "Date: " + item['pub_date']
        print "Word count: " + item['word_count']
        print "Subsection: " + str(item['subsection_name'])
        for kw in item['keywords']:
            print kw['name']
            print kw['value']
        sleep(2)
        print
        # br.open(item['web_url'])
        # print br.title()
        # soup = BeautifulSoup(br.response(),"html5lib")
        # print soup.prettify()
print "----- End the crawl -----"
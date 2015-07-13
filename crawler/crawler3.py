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

print "----- Begin the crawl -----"
for i in range(0, 1):
    querysrc = [opening, startdate, enddate, page+str(i), key]
    query = "&".join(querysrc)
    print "----- " + query + " -----"
    jstrs = urllib2.urlopen(query).read()
    t = jstrs.strip('()')
    tss= json.loads( t )  # error no joson object
    print "PAGE: " + str(i)
    for item in tss['response']['docs']:
        print item['web_url']
        print item['lead_paragraph']
        sleep(2)
        print
        # br.open(item['web_url'])
        # print br.title()
        # soup = BeautifulSoup(br.response(),"html5lib")
        # print soup.prettify()
print "----- End the crawl -----"
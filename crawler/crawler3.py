import urllib2
import json
import mechanize
import csv
import datetime
from time import *
from functools import wraps

opening = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name%3AWorld+OR+section_name%3AU.S."
page = "page="
key = "api-key=57a53bc0e5186e9d1ae82fbeed6b3238:7:72493178"
out = open("data_NYT.csv", "wb")
writer = csv.writer(out, delimiter=",")

def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry

    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck, e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print msg
                    sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry

def crawldate(date):
    startdate = "begin_date=" + date
    enddate = "end_date=" + date
    print "----- Crawling for " + date + " -----"
    for i in range(pagestart, limit):
        querysrc = [opening, startdate, enddate, page+str(i), key]
        query = "&".join(querysrc)
        print "----- " + query + " -----"
        jstrs = urlopen_with_retry(query)
        t = jstrs.strip('()')
        tss= json.loads( t )  # error no joson object
        print "PAGE: " + str(i) + "   started from " + str(pagestart)

        if len(tss['response']['docs']) == 0:
            print "Finished"
            return

        for item in tss['response']['docs']:
            # print item['web_url']

            # Some funny exception
            if 'main' not in item['headline']:
                continue

            print "Headline: " + str(item['headline']['main'].encode('utf-8'))
            # print "Content: " + str(item['lead_paragraph'].encode('utf-8'))
            # print "Date: " + str(item['pub_date'].encode('utf-8'))
            # print "Word count: " + str(item['word_count'].encode('utf-8'))
            # print "Subsection: " + str(item['subsection_name'].encode('utf-8'))

            # Checks for nones
            if item['lead_paragraph'] is None:
                 item['lead_paragraph'] = item['snippet']
            if item['subsection_name'] is None:
                item['subsection_name'] = ""
            if item['headline']['main'] is None:
                item['headline']['main'] = ""
            if item['section_name'] is None:
                item['section_name'] = ""
            if item['lead_paragraph'] is None:
                item['lead_paragraph'] = ""
            if item['word_count'] is None:
                item['word_count'] = "0"
            if item['pub_date'] is None:
                item['pub_date'] = ""
            if item['byline'] is None:
                item['byline'] = ""

            if len(item['byline']) != 0:
                output = [item['headline']['main'].encode('utf-8'), item['section_name'].encode('utf-8'), item['subsection_name'].encode('utf-8'), item['pub_date'].encode('utf-8'), item['word_count'].encode('utf-8'), item['lead_paragraph'].encode('utf-8'), item['byline']['original'].encode('utf-8')]
            else:
                # print item['lead_paragraph']
                output = [item['headline']['main'].encode('utf-8'), item['section_name'].encode('utf-8'), item['subsection_name'].encode('utf-8'), item['pub_date'].encode('utf-8'), item['word_count'].encode('utf-8'), item['lead_paragraph'].encode('utf-8')]
            writer.writerow(output)
            # br.open(item['web_url'])
            # print br.title()
            # soup = BeautifulSoup(br.response(),"html5lib")
            # print soup.prettify()
        # sleep(0.1)
    print "----- Crawled " + date + " -----"

# br = mechanize.Browser()
# print "----- Doing the login -----"
# br.open("https://myaccount.nytimes.com/auth/login")
# print br.title()
# br.select_form(nr=0)
# br.form['userid'] = "markleechuyong@gmail.com"
# br.form['password'] = "musicshare"
# br.submit()
# print "----- Login success -----"

@retry(urllib2.URLError, tries=4, delay=3, backoff=2)
def urlopen_with_retry(query):
    return urllib2.urlopen(query).read()

pagestart = 0
limit = 20000

print "----- Begin the crawl -----"

c_date = datetime.datetime(2014,4,8)

for i in range(0, 366):
    c_date -= datetime.timedelta(days=1)
    query_date = c_date.strftime("%Y%m%d")
    crawldate(query_date)


#crawldate("20150101")
print "----- End the crawl -----"

out.close()
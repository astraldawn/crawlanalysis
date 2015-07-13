from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# uncomment if using Firefox web browser
driver = webdriver.Firefox()

# uncomment if using Phantomjs
# driver = webdriver.PhantomJS()

url = "http://www.nytimes.com"
driver.get(url)

# print driver.find_element_by_tag_name('a')

# go to the google home page
# driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
sleep(5)
print driver.title

'''
# set initial page count
pages = 1
with open('myURLs.txt', 'w') as f:
    while True:
        try:
            # sleep here to allow time for page load
            sleep(2)
            # grab the Next button if it exists
            # btn_next = driver.find_element_by_name("shell")
            # print btn_next
            # find all item-title a href and write to file
            print "Attempt to load"
            print driver
            print driver.title
            # links = driver.find_elements_by_class_name('element2')
            # print links
            # print "Page: {} -- {} urls to write...".format(pages, len(links))
            # for link in links:
            #     f.write(link.get_attribute('href')+'\n')
            # # Exit if no more Next button is found, ie. last page
            # if btn_next is None:
            #     print "crawling completed."
            #     exit(-1)
            # # otherwise click the Next button and repeat crawling the urls
            # pages += 1
            # btn_next.send_keys(Keys.RETURN)
        # you should specify the exception here
        except:
            print "Error found, crawling stopped"
            exit(-1)
'''
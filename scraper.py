# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# import the scraperwiki library to store data
import scraperwiki
import lxml.html
print "hello world"
#here i create a variable
myname = "leo"
print myname
# # Read in a page
#scrape is a fuction from the scraperwiki library then need the url as value scraperwiki is a library that we got by putting import scraperwiki
# print html show the code on the morph.io page meaning displays it VARIABLES HAS THE =SIGN, FUNCTION IS BETWEEN BRACKETS
html = scraperwiki.scrape("http://foo.com")  
print html
# # Find something on the page using css selectors
# ROOT BELOW TAKE THE CODE FROM THE PRINT HTML AND CONVERT PROBLEM IS WE DID NOT IMPORT LXML LIBRARY SO WE NEED TO UNCOMMENT THE LINE IMPORT
LXML
root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

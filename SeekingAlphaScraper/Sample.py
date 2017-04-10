__author__ = 'phani'

t="Google's long term problem is the declining quality of its crown jewel - its browser. The bulk of Google's revenue still derives fro advertising revenues around its browser which still maintains a market share of over 70%.This will" \
  "decline long term partially fur to mobil which is the author's point.The main issue for me is the Google search engine is becoming less and less usable due to the" \
  "prepaid ranking of search results.A prime exmple is my search for a restaurants web site.Using Google search the restaurant's own web site can" \
  "usually be found on page three of the search results. What are the first two pages ? Yelp and twenty other rating sites that paid for their place in line. " \
  "The point is I dont use Googles search nearly as often now. Where do I go? Less commercialized search engines or worse for Google-Facebook" \
  "May be i am overreacting to my persional experience but i have friends coming to the same conclusion"

from urllib.request import urlopen
from urllib.parse import urlencode

def getSentiment(t):
  data = urlencode({"text": t})
  binary_data = data.encode('UTF-8')
  u = urlopen("http://text-processing.com/api/sentiment/", binary_data)
  the_page = u.read().decode('UTF-8')
  print(the_page)

getSentiment(t)
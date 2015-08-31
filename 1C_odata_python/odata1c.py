import urllib2
import feedparser
import requests

class service(interceptor):

    def __init__(self, url, login, password):
        self.url = url
        self.req = requests.get(url+'Document_Order', auth=(login, password))

    def execute(self):
        proc_url = self.url + "/" + self.property
        result = feedparser.parse(proc_url)
        for entry in result.entries: print entry.title




class interceptor(object):
    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except:
            self.property = name
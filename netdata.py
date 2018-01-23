import urllib2

webUrl = urllib2.urlopen("https://vibrantbells.tumblr.com")
print "result code: " + str(webUrl.getcode());

data = webUrl.read()
print data;

# code for retrieving data from the internet
#
# import urllib2
#
# def main():
#
#     # open a connection to URL using urllib2
#     webUrl = urllib2.urlopen("http://joemarini.com")
#
#     # get result code and print it
#     print "result code: " + str(webUrl.getcode())
#
#     # read the data from the url and print it
#     data = webUrl.read()
#     print data
#
# if __name__ == '__main__':
#     main()


# Working with JSON data = javascript object notation

# example code for parsing and processing JSON

import urllib2
import json

def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]

        count = theJSON["metadata"]["count"];
        print str(count) + " events recorded"

        # for each event, print the place where it occured
        for i in theJSON["features"]:
            print i["properties"]["place"]

        # print the events that only have a magnitude greater than 4
        for i in theJSON["features"]:
            if i ["properties"]["mag"] >= 4.0:
                print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]

        # print only events where at least 1 person reported feeling it
        print "Events that were felt: "
        for i in theJSON["features"]:
            feltReports = i["properties"]["felt"]
            if (feltReports != None) and (feltReports > 0):
                print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], \
                    " reported " + str(feltReports) + " times"

def main():
    # define a variable to hold and source URL
    # in this case we'll use the free data feed from the USGS
    # this feed lists all eartquakes for the last day larger than Magnitude 2.5

    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # open the URL and read the data
    webUrl = urllib2.urlopen(urlData)
    print webUrl.getcode()

    if (webUrl.getcode() == 200):
        data = webUrl.read()
        # print customized results
        printResults(data)

    else:
        print "Recieved an error from the server, cannot retrieve resutls" + str(webUrl.getCode)

if __name__ == '__main__':
    main()
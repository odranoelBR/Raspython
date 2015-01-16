
import urllib2
class RoboControllerApi:

    def moveFront(self):
        url = 'http://10.5.5.1/front'
        response = urllib2.urlopen(url).read()

    def moveBack(self):
        url = 'http://10.5.5.1/back'
        response = urllib2.urlopen(url).read()

    def moveLeft(self):
        url = 'http://10.5.5.1/left'
        response = urllib2.urlopen(url).read()

    def moveRight(self):
        url = 'http://10.5.5.1/right'
        response = urllib2.urlopen(url).read()

    def testConnection(self):
        url = 'http://10.5.5.1/test'
        response = urllib2.urlopen(url).read()
from bs4 import BeautifulSoup, SoupStrainer
from urllib2 import urlopen
import re

#Check if the var contains a valid place
def check_if_place(place):
    if(place != None):
        return True
    else:
        return False



    

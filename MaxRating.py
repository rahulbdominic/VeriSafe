from bs4 import BeautifulSoup, SoupStrainer
from urllib2 import urlopen
import re

def get_maxrating(Mdata):

    #Get max rank in array and assign entire element to max_element
    max_element = Mdata[0]
    print(Mdata)
    for i in range(len(Mdata)):
        if float(Mdata[i][2]) > float(max_element[2]):
            print(max_element)
            max_element = Mdata[i]

    #Get index of element
    max_element_index = 0
    max_element_index = Mdata.index(max_element)

    #Return index of element
    return max_element_index

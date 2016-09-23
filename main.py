from urllib2 import urlopen
from ifexist import check_if_place
from TitleAnalyse import analyse_title
from ContentAnalyse import analyse_content
from MergeRanks import merge_ranks
from bs4 import BeautifulSoup
from MaxRating import get_maxrating

import re

def parse(url, source):

    #Parse HTML using BeautifulSoup
    soup = BeautifulSoup(urlopen(url))

    #Check URL source
    if source == 'CNN MAIN':

        #Extract date, title and content
        article_date = soup.find('div', {'class': 'cnn_strytmstmp'}).text
        article_title = soup.find('div', {'id':'cnnContentContainer'}).find('h1').text.encode('utf-8')
        paragraphs = soup.find('div', {'class':'cnn_strycntntlft'}).find_all('p')
        article_content = ('').join([ str(paragraph.text.encode('utf-8')) for paragraph in paragraphs])

        #Try to get offical location
        article_place = paragraphs[0].find('strong').text.encode('utf-8')

        #If text exists, return it.
        if (article_place != None):
            return [article_date, article_title, article_content, article_place]
        else:
            return [article_date, article_title, article_content]

    elif source == 'TOI MAIN':

        #Extract date, title and content
        raw_article_date = str(soup.find('span', {'class': 'byline'}).text.encode('utf-8'))
        article_title = str(soup.find('span', {'class': 'arttle'}).find('h1').text.encode('utf-8'))
        raw_article_content = str(soup.find('div', {'class': 'Normal'}).text.encode('utf-8'))

        #Try to get offical location
        
        try :
            article_date = (raw_article_date.split('|')[1]).strip()
        except:
            article_date = raw_article_date

        try :
            article_place = raw_article_content.split(':')[0]
        except:
            article_place = None

        try :            
            article_content = raw_article_content.split(':')[1]
        except:
            article_content = raw_article_content
        
        #If text exists, return it.
        if(article_place != None):
            return [article_date, article_title, article_content, article_place]
        else:
            return [article_date, article_title, article_content]


#Set URL
print('Enter url: ')
url = str(raw_input())

#Get HTML data from URL
print('Enter source: ')
source = str(raw_input())
response = parse(url, source)

#Extract content from response
article_date = response[0]
article_title = response[1]
article_content = response[2]
article_place = response[3]

#Location dictionary
dictionary = ['BANGALORE', 'Bangalore', 'Bellary', 'Mysore', 'Chennai', 'Delhi']

final_place = ''
if(check_if_place(article_place) == True):
    final_place = article_place
else:
    #RUN ALGORITHMS

    #Analyse ranked content separately
    Tdata = analyse_title(article_title, [], dictionary)
    Cdata = analyse_content(article_content, [], dictionary, 'C')
    print(Cdata)
    Gdata = analyse_content(article_content, [], dictionary, 'G')

    #Merge ranked content
    Mdata = merge_ranks(Cdata, Gdata, Tdata)
    
    #Get location of max rating in array
    max_element_index = get_maxrating(Mdata)
    final_place = Mdata[max_element_index][0]

print final_place

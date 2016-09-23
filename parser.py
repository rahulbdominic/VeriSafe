from bs4 import BeautifulSoup
from urllib2 import urlopen
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
        raw_article_content = str(soup.find('div', {'id':'artext1'}).find('div', {'class': 'Normal'}).text.encode('utf-8'))

        #Try to get offical location
        article_date = (raw_article_date.split('|')[1]).strip()
        article_place = raw_article_content.split(':')[0]
        article_content = raw_article_content.split(':')[1] 

        #If text exists, return it.
        if(article_place != None):
            return [article_date, article_title, article_content, article_place]
        else:
            return [article_date, article_title, article_content]

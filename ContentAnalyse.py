from urllib2 import urlopen
import re

def analyse_content(data, ls, location_dict, mode):
    s = modifytext(data)
    
    #Add each word in data to new element of array
    splitdata = s.split(' ')
    newls = []
    #Check if it is a general search or comma search
    if(mode == 'G'):
        
        for i in range(len(splitdata)):
            #Check for words in dictionary and update list
            presult = checkplace(splitdata[i], location_dict)
            if(presult == True):
                newls = updateList(splitdata[i], ls, 0.4)
                
    elif(mode == 'C'):
        for i in range(len(splitdata)):
            if(splitdata[i] == ','):
                
                #Check for words in dictionary[before and after comma] and update list
                presult = checkplace(splitdata[i - 1], location_dict)
                resultp = checkplace(splitdata[i + 1], location_dict)
                if(presult == True):
                    newls = updateList(splitdata[i - 1], ls, 0.5)
                if(resultp == True):
                    newls = updateList(splitdata[i + 1], ls, 0.5)
    return newls

#Modify data to add spaces before ',' to allow split to work
def modifytext(data):
    strlen = len(data)
    newstr = ''
    #Add to newstr word by word except add space before letter if ',' is detected
    for i in range(strlen - 1):
        if(data[i] == ','):
            newstr += ' '
        if(data[i] == '-'):
            newstr += ' '
        newstr += str(data[i])
        if(data[i] == '-'):
            newstr += ' '
    return newstr

def updateList(presult, ls, weight):
    done = False
    
    #Run through and check the physical location of each element in the array
    for j in range(len(ls)):
        if (len(ls)):
            
            #If place found then increase the occurance count
            if(ls[j][0] == presult):
                count = int(ls[j][1])
                count += 1
                ls[j][1] = count

                #Change ranking
                rank = count * weight
                ls[j][2] = str(rank)
                done = True
                
    #If not found then append array
    if(done == False):
        ls.append([presult, '1', str(weight)])
    return ls

def checkplace(s, place_Dictionary):
    
    #Cross reference the dictionary with the string
    for i in range(len(place_Dictionary)):
        if(place_Dictionary[i] == s):
            return True
    return False

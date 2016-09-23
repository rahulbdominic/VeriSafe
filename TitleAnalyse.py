from urllib2 import urlopen
import re

def analyse_title(data, ls, location_dict):
    s = modifytext(data)
    #Add each word in data to new element of array
    splitdata = s.split(' ')
    newls = []

    #Check if any word is a in dictionary and update list
    for i in range(len(splitdata)):
        presult = checkplace(splitdata[i], location_dict)
        if(presult == True):
            newls = updateList(splitdata[i], ls)

    return newls
    

#Modify data to add spaces before ',' to allow split to work
def modifytext(data):
    strlen = len(data)
    newstr = ''
    
    #Add to newstr word by word except add space before letter if ',' is detected
    for i in range(strlen - 1):
        if(data[i] == ','):
            newstr += ' '
        newstr += str(data[i])
    return newstr

def updateList(presult, ls):
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
                weight = 0.7
                rank = count * weight
                ls[j][2] = str(rank)
                done = True
                
    #If not found then append array
    if(done == False):
        ls.append([presult, '1', '0.7'])
    return ls

def checkplace(s, place_Dictionary):
    
    #Cross reference the dictionary with the string
    for i in range(len(place_Dictionary)):
        if(place_Dictionary[i] == s):
            return True
    return False

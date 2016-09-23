from urllib2 import urlopen
import re

def merge_ranks(Cdata, Gdata, Tdata):

    #Create new array to hold merged values
    Mdata = []
    
    #Find the largest array out of the 3
    c = (len(Cdata))
    g = (len(Gdata))
    t = (len(Tdata))
    compare = [c, g, t]
    maxindex = compare.index(max(compare))

    #Copy largest array floato Mdata
    if(maxindex == 0):
        #If Cdata is greatest, call ifComma
        Mdata = ifComma(Cdata, Tdata, Gdata)
        
    elif(maxindex == 1):
        #If Gdata is greatest, call ifGeneral
        Mdata = ifGeneral(Gdata, Tdata, Cdata)
                
    else:
        #If Tdata is greatest, call ifTitle
        Mdata = ifTitle(Tdata, Cdata, Gdata)
        
    return Mdata

def ifComma(Cdata, Tdata, Gdata):

    Mdata = Cdata
    #CDone is present to check if match is found after loop
    CDone = False
    #Check if element in Mdata is present in Gdata
    for i in range(len(Gdata)):
        for j in range(len(Mdata)):
            #If present, update rank and count
            if(Gdata[i][0] == Mdata[j][0]):
                GRank = float(Gdata[i][2])
                MRank = float(Mdata[j][2])
                Mdata[j][2] = str(GRank + MRank)
                #Update count
                Mdata[j][1] = str(int(Gdata[i][1]) + int(Mdata[j][1]))
                
                CDone = True
        #If not present then append Mdata to include element
        if(CDone != True):
            Mdata.append([Gdata[i][0], Gdata[i][1], Gdata[i][2]])
        else:
            CDone = False

    #Check if element in Mdata is present in Tdata
    for k in range(len(Tdata)):
        for l in range(len(Mdata)):
            #If present, update rank
            if(Tdata[k][0] == Mdata[l][0]):
                TRank = float(Tdata[k][2])
                MRank = float(Mdata[l][2])
                Mdata[l][2] = str(TRank + MRank)
                #Update count
                Mdata[l][1] = str(int(Tdata[k][1]) + int(Mdata[l][1]))
                
                CDone = True
        #If not present then append Mdata to include element
        if(CDone != True):
            Mdata.append([Tdata[k][0], Tdata[k][1], Tdata[k][2]])
        else:
            CDone = False

    #Return merged list
    return Mdata


def ifGeneral(Gdata, Tdata, Cdata):
    
    Mdata = Gdata
    #GDone is present to check if match is found after loop
    GDone = False

    #Check if element in Mdata is present in Cdata
    for i in range(len(Cdata)):
        for j in range(len(Mdata)):
            #If present, update rank
            if(Cdata[i][0] == Mdata[j][0]):
                CRank = float(Cdata[i][2])
                MRank = float(Mdata[j][2])
                Mdata[j][2] = str(CRank + MRank)
                #Update count
                Mdata[j][1] = str(int(Cdata[i][1]) + int(Mdata[j][1]))
                
                GDone = True
        #If not present then append Mdata to include element
        if(GDone != True):
            Mdata.append([Cdata[i][0], Cdata[i][1], Cdata[i][2]])
        else:
            GDone = False

    #Check if element in Mdata is present in Tdata
    for i in range(len(Tdata)):
        for j in range(len(Mdata)):
            #If present, update rank
            if(Tdata[i][0] == Mdata[j][0]):
                TRank = float(Tdata[i][2])
                MRank = float(Mdata[j][2])
                Mdata[j][2] = str(TRank + MRank)
                #Update count
                Mdata[j][1] = str(int(Tdata[i][1]) + int(Mdata[j][1]))
                
                GDone = True
        #If not present then append Mdata to include element
        if(GDone != True):
            Mdata.append([Tdata[i][0], Tdata[i][1], Tdata[i][2]])
        else:
            GDone = False

    #Return merged list
    return Mdata


def ifTitle(Tdata, Cdata, Gdata):

    Mdata = Tdata
    #TDone is present to check if match is found after loop
    TDone = False
    #Check if element in Mdata is present in Gdata
    for i in range(len(Gdata)):
        for j in range(len(Mdata)):
            #If present, update rank
            if(Gdata[i][0] == Mdata[j][0]):
                GRank = float(Gdata[i][2])
                MRank = float(Mdata[j][2])
                Mdata[j][2] = str(GRank + MRank)
                #Update count
                Mdata[j][1] = str(int(Gdata[i][1]) + int(Mdata[j][1]))
                
                CDone = True
        #If not present then append Mdata to include element
        if(TDone != True):
            Mdata.append([Gdata[i][0], Gdata[i][1], Gdata[i][2]])
        else:
            TDone = False

    #Check if element in Mdata is present in Cdata
    for i in range(len(Cdata)):
        for j in range(len(Mdata)):
            #If present, update rank
            if(Cdata[i][0] == Mdata[j][0]):
                CRank = float(Cdata[i][2])
                MRank = float(Mdata[j][2])
                Mdata[j][2] = str(CRank + MRank)
                #Update count
                Mdata[j][1] = str(int(Cdata[i][1]) + int(Mdata[j][1]))
                
                TDone = True
        #If not present then append Mdata to include element
        if(TDone != True):
            Mdata.append([Cdata[i][0], Cdata[i][1], Cdata[i][2]])
        else:
            TDone = False

    #Return merged list
    return Mdata

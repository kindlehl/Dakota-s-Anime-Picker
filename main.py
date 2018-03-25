import requests
import random
import string
import re

def getContent(URL = "http://animefreak.tv"):
    response = requests.get(URL)
    return response.text

def pruneString(myStr):
    query = "href=\"/watch/"
    query2 = '>'
    pruned = [] 

    for line in myStr.splitlines():
        index = line.rfind(query)
        if (index != -1):
            #Relevant line found
            index2 = line.find(query2, index)
            if (index2 != -1):
                pruned.append(line[index2+1:line.find("<", index2+1)])
    return pruned

    
def main():
    contentString = getContent()
    titleList = pruneString(contentString);  
    print("Found ", len(titleList), " Titles")
    boring = True
    while(boring):
        maybeGood = titleList[random.randint(0, len(titleList)-1)]
        print("Found title: ", maybeGood)
        char = input(" press q to quit or anything else to get a new title")
        if char == "q":
            boring = False

main()

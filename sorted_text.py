#!/usr/bin/env python
import sys
import re
import nltk
from nltk.tokenize import wordpunct_tokenize
import string

word_dict = {}
punct_dict = {}
punct_list = []
punct_str = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for line in sys.stdin:
    #strip white spaces at beginning and end of each line and make lowercase
    line = line.strip().lower()
    #remove any numbers from each line
    line = re.sub(r'\d+', '', line)
    #separate words by spacing
    words = line.split(" ")
    
    #build a dictionary of only words (no punctuation) and their counts
    for word in words:
        #remove punctuation from each word while keeping word intact
        punct_free = re.sub(r'[^\w\s]', '', word)
        #avoid adding "words" that were made up only of punctuation so they are not counted
        if punct_free == '':
            continue
        #add 1 to the count when a word reappears
        elif punct_free in word_dict:
            word_dict[punct_free]+=1
        #attach a count of 1 to each word in text  
        else:
            word_dict[punct_free]=1

    #build a list of all punctuation characters in text
    for word in words:
        #break word into list of characters
        for char in word: 
            if char in punct_str:
                punct_list=punct_list+[char]
        
#build a dictionary of all punctuation in text and their counts
for punct in punct_list:
    if punct in punct_dict:
        punct_dict[punct]+=1
    else:
        punct_dict[punct]=1

#merge word and punctuation dictionaries
word_dict.update(punct_dict)

# sort merged dictionary by values in descending order
sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

for i in sorted_dict:
	print(i[0], i[1])
#!/usr/bin/env python
import sys
import re
import nltk
from nltk.tokenize import wordpunct_tokenize
import string

#stdin = standard input
for line in sys.stdin:
    try:
        #strip white spaces at beginning and end of each line and make lowercase
        line = line.strip().lower()
        #remove any numbers from each line
        line = re.sub(r'\d+', '', line)
        #separate words and punctuation
        tokens = nltk.wordpunct_tokenize(line)
        #separate tokens that are strings of punctuation into individual characters
        try:
            for token in tokens:  #creating a new tokens list where each character that is punctuation is a separate token
                punc_list=[]
                #find tokens that are strings of punctuation
                if str(token).isalpha()==False:
                    #make each character of the string a separate token (for counting)
                    [punc_list.append(i) for i in str(token)]
                    #remove string of multiple punctuation 
                    tokens.remove(token)
                    #tokens.append(punc_list)
        except Exception as e:
            print(e)

        try:
            for token in tokens:    #loop through new tokens list
                #assign a value of 1 to each token
                print(token + "\t1")
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
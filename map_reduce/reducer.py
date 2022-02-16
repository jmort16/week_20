#!/use/bin/env python
import sys

current_word =  None
current_count = 0
word = None

#take all the words from the mapper and count them

#lines passes from the mapper.py program
for line in sys.stdin:
    line=line.strip()

    word,count = line.split("\t", 1)

    count = int(count)

    # sorted values from command line are passed in, and 
    # if we have multiple of the same word, we increment the count
    if current_word == word:
        current_count += count
    else:
        # if there is a current word and it's not None (which was how we instantiated it)
        if current_word:
            print(current_word + "\t" + str(current_count))

        current_count = count
        current_word = word

if current_word == word:
    print(current_word + "\t" + str(current_count))

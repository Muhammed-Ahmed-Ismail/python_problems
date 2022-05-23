#! /usr/bin/env python3
import sys
import os

filename = sys.argv[1]

file = open(filename, "r")
content = file.read()
number_of_words = 20
search_arr = sorted(content.split(" "))
count = []
popular_words = []
counter = 0
for x in range(0, len(search_arr) - 2):
    if search_arr[x] == search_arr[x + 1]:
        counter += 1
    else:
        counter += 1
        if len(count) >= number_of_words:
            if counter > min(count):
                min_c = min(count)
                index = count.index(min_c)
                popular_words[index] = search_arr[x]
                count[index] = counter
                counter = 0
            else:
                counter = 0
                continue
        else:
            popular_words.append(search_arr[x])
            count.append(counter)
            counter = 0

result ="";
for index,word in enumerate(popular_words):
    result+=str(index+1)+'-'+word+'\n'
file=open('result','w')

file.write(result)
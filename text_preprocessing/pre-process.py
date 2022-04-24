import csv
from collections import defaultdict
import sys
import csv

csv.field_size_limit(sys.maxsize)

columns = defaultdict(list) # each value in each column is appended to a list

def csv2txt():
    with open('guruchandali_haridas.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

    with open("guruchandali_haridas.txt", "w") as text_file:
        print(len(columns['text1']))
        for i in columns['Text1']:
        #print(str(i) + '\n')
            text_file.write(str(i) + '\n')
    text_file.close()

def count_words(file_name):
    file = open(file_name, "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))

def tokenize(input_file, output_file):
    lst = []
    output = []

    with open(input_file, "r") as input_file:
        for line in input_file:
            lst = line.strip('।').split('।')
            for i in lst:
                output.append(i + '\n')

    with open(output_file, "w") as output_file:
        for i in output:
            i = ' '.join(i.split())
            if i == '\n' or i == '\t' or i == ' ' or i.startswith('সর্বশেষ এডিট :'):
                continue
            output_file.write(i + '\n')
    input_file.close()
    output_file.close()

#def remove_punctuations():

def remove_character(in_file_name, out_file_name, character):
    in_file = open(in_file_name, "rt")
    data = in_file.read()
    data = data.replace(character, "")
    out_file = open(out_file_name, "w")
    out_file.write(data)
    in_file.close()
    out_file.close()

#count_words("sumono.txt")
#csv2txt()
#tokenize("sumono.txt", "tokenized_sumono.txt")
remove_character("no_punc_sumono.txt", "no_punc_sumono_v1.txt", "﻿")


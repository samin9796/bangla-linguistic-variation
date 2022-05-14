import nltk
from collections import Counter


def count_words(file_name):
    file = open(file_name, "rt")
    data = file.read()
    words = data.split()
    print('Number of words in text file :', len(words))


def count_ngrams(in_file_name, out_file_name):   
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    ngramfdist = nltk.FreqDist()
    threegramfdist = nltk.FreqDist()
    for line in in_file:
        if len(line) > 2:
            tokens = line.strip().split(' ')

            n_grams = nltk.ngrams(tokens, 3)
            ngramfdist.update(n_grams)
    cnt = 0
    for k,v in ngramfdist.most_common():
        out_file.write(str(k) + ' ' + str(v) + '\n')
        cnt+=1
        if cnt > 30:
            break
    #print(bigramfdist.most_common())


def word_count(fname, outfile, lst):
    with open(fname, "rt") as f, open(outfile, "w") as out:
        newList = Counter(f.read().split())
        for i in lst:
            out.write(str(i) + " " + str(newList[i]) + "\n")
    out.close()


#word_count("clean_wb.txt", "clean_wb_word_freq_new.txt", lst = ["বের হয়", "বেরোয়", "থিতিয়ে গেছে", "দাদা", "অনুরোধ", "আবদার", "অকাল", "অসময়", "অলস", "কুঁড়ে", "ঈর্ষা", "হিংসা", "হাওয়া", "বাতাস", "লবণ", "নূন", "গোসল", "স্নান", "ভাবি", "বৌদি", "রোজ", "প্রতিদিন", "বিকাল", "বিকেল", "ঠাকুরমা", "দিদা", "দাদি", "পূজা", "পূজো", "যলদি", "জলদি", "তাড়াতাড়ি", "কুমড়া", "কুমড়ো", "সর্ষে", "সরষে", "সরিষা", "মরিচ", "লঙ্কা", "আস্ত", "গোটা", "চুলা", "চুলো", "উনুন", "বোন", "দিদি", "দুরকম", "দুইরকম", "ইচ্ছা", "বাসনা", "খতম", "শেষ", "অভ্যাস", "অভ্যেস", "হাঁড়ি", "পাতিল", "ফুপ্পি", "পিসি", "পিষি", "ভগমান", "ঈশ্বর", "আল্লাহ", "খারাপ", "মন্দ", "কিপটা", "কিপটে", "নাই", "নেই", "শুকনা", "শুকনো", "কুরুক্ষেত্র", "যুদ্ধ", "সুন্দর", "দারুণ", "মজা", "ইয়ার্কি", "সবে", "এইমাত্র", "জিরা", "জিরে", "তেষ্টা", "তৃষ্ণা", "কৌটা", "কৌটো", "পৌষ্য", "পোষা", "মিথ্যা", "মিথ্যে", "তিনি", "উনি", "ইনি" ])
#count_words("clean_bd.txt")
#count_words("clean_wb.txt")
count_ngrams("clean_bd.txt", "3gram_bd.txt")
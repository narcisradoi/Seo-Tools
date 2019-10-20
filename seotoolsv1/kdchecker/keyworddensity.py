
import re 

filename = "newfile.txt"

with open(filename) as f:
    text = f.read()

wd_count = 0
match_count = 0

def count_words():
    global wd_count
    my_regex = r"\S+"
    all_matches = re.findall(my_regex, text)
    wd_count = len(all_matches)
    
count_words()

def count_word_times (word):
    global match_count
    my_regex = r"("+ re.escape(word) + r")"
    word_matches = re.findall(my_regex, text)
    match_count = len(word_matches)

count_word_times("guna")

def keyword_percentage():
    global perc
    try:
        perc = match_count*100/wd_count
        perc = str(round(perc,2))
    except ZeroDivisionError:
        print("Divided by 0")
    return perc

keyword_percentage()
#to create a dictionary

import json
import difflib

data=json.load(open("data.json"))

def value_access(w):
    w = w.lower()

    if w in data:
        value=data[w]
        for item in value:
            print(item)
    elif len(difflib.get_close_matches(w,data.keys(),cutoff=0.8))>0:
        expw = (difflib.get_close_matches(w,data.keys(),cutoff=0.8))[0]
        print("Did you mean: "+expw)
        check=(input("Press Y else N")).upper()
        if check=="Y":
            for item in data[expw]:
                print(item)
        else:
            print("Please check the word again. No matches found.")
    else:
        print("Please check the word again. No matches found.")


word=input("Enter a word:\n")
value_access(word)

#-*- coding: utf-8 -*-
def hindi_stem(word):
    suffixes ={
        5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
        4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
        3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
        2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
        1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    }

     
    for i in suffixes:
        if len(word)>i+1:
            for j in suffixes[i]:
                if  word.endswith(j):
                    return word[:-i]
    return word

#print("Enter the hindi word")
#word=raw_input()
words=["अँक","अँग्रेज़ी","अंकलमंदी","अंकुल","अंगनाई"]
for word in words:
    print(hindi_stem(word))

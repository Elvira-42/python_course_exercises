"""#The code below contains a list of words. Build a dictionary that contains all these words as keys,
# and their quantities as values. Print the words with their quantities.

wordlist = ["apple","durian","banana","durian","apple","cherry",
    "cherry","mango","apple","apple","cherry","durian","banana",
    "apple","apple","apple","apple","banana","apple"]

d={}
for i in wordlist:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""


"""#The code block below contains a string that is a list of words, separated by commas.
# Build a dictionary that contains all these words as keys, and how often they occur as values.
# Then print the words with their quantities.

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
    "apple,apple,cherry,durian,banana,apple,apple,apple," + \
    "apple,banana,apple"

d={}
words=text.split(",")
for i in words:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""


"""#The code block below contains a very small dictionary that contains the translations of English words to Dutch.
# Write a program that uses this dictionary to create a word-for-word translation of the given sentence.
# A word for which you cannot find a translation, you can leave “as is.” The dictionary is supposed
#to be used case-insensitively, but your translation may consist of all lower case words.
# It is nice if you leave punctuation in the translation, but if you take it out, that is acceptable.

english_dutch = { "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
    "zaag", "first":"eerst", "performance":"optreden", "of":"van",
    "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
    "one":"een", "world":"wereld", "leading":"leidend", "modern":
    "modern", "composer":"componist", "composers":"componisten",
    "two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson."

def En_DutchTranslator(text,dictionary):
    translated=""
    text=text.lower()
    cleantxt=""
    for i in text:
        if i>="a" and i<="z":
            cleantxt+=i
        else:
            cleantxt+=" "
    splittxt=cleantxt.split(" ")
    for i in splittxt:
        if i not in dictionary:
            translated+=i+" "
        else:
            translated+=dictionary[i] + " "
    return translated

translation=En_DutchTranslator(sentence,english_dutch)
print(translation)
"""


#Exercise 13.2
#Thecodeblockbelowshowsalistofmovies. For each movie it also shows a list of ratings.
# Convert this code in such a way that it stores all this data in one dictionary,
# then use the dictionary to print the average rating for each movie, rounded to one decimal.

movies = ["Monty Python and the Holy Grail",
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

grail_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5,8 ]
brian_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]
life_ratings = [ 7, 6, 5 ]
different_ratings = [ 6, 5, 6, 6 ]

ratings=[grail_ratings,brian_ratings,life_ratings,different_ratings]

MontyPython={}
for i in range(len(ratings)):
    MontyPython[movies[i]]=ratings[i]


for movies in MontyPython.keys():
    avgRating=sum(MontyPython[movies])/len(MontyPython[movies])
    print("The average rating for the movie {} is {}".format(movies,avgRating))

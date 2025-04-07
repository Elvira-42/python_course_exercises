"""#Write a program that reads the lines from“pc_rose.txt,” and displays only those lines that contain the word "name".

h=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_rose.txt")
while True:
    buffer=h.readline()
    if "name" in buffer:
        print(buffer)
    if buffer=="":
        break
h.close()"""

"""#Write some code that counts how often the word “jabberwock” (with any capitalization) occurs
# in the first 5 lines of the file "pc_jabberwocky.txt". Print only the number of occurrences of that word.
# Once it works, remove the count so that you count the number of occurrences of the word in the text as a whole.

h=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_jabberwocky.txt")
i=0
N_jabberwocks=0
while i<=1:
    buffer=h.readline()
    N_jabberwocks+=buffer.count("JABBERWOCK")
    N_jabberwocks+=buffer.count("jabberwock")
    i+=1
print(N_jabberwocks)
h.close()
"""

"""#Write a program that reads the contents of “pc_rose.txt,” and writes exactly the same contents
# to the file “pc_writetest.tmp.” Then open the file “pc_writetest.tmp” and display the contents.

h=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_rose.txt")
lines=h.readlines()
h.close()

h=open("pc_writetest.tmp","w")
h.writelines(lines)
h.close()
h1=open("pc_writetest.tmp")
buffer=h1.read()
print(buffer)
h1.close()



#Write a program that reads the contents of “pc_rose.txt,” reverses each of the lines,
# and writes the reversed lines to the file “pc_writetest.tmp.”
# Then open the file “pc_writetest.tmp” and display the contents.

h=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_rose.txt")
h1=open("pc_writetest.tmp","w")
while True:
    buffer=h.readline()
    if buffer=="":
        break
    reffub=""
    for i in range(len(buffer)-1,-1,-1):
        reffub+=buffer[i]
    h1.write(reffub)

h.close()
h1.close()
h1=open("pc_writetest.tmp")
r=h1.read()
h1.close()
print(r)
"""


"""#Exercise 16.1
#Write a program that reads the contents of the file “pc_woodchuck.txt,” splits it into words
# (where everything that is not a letter is considered a word boundary), and case-insensitively
# builds a dictionary that stores for every word how often it occurs in the text.
# Then print all the words with their quantities in alphabetical order.

h=open("pc_woodchuck.txt")
woodchuck=h.read()
h.close()

def cleanText(text):
    text=text.lower()
    cleantext=""
    for ch in text:
        if ch>="a" and ch<="z":
            cleantext+=ch
        else:
            cleantext+=" "
    return cleantext



def dictionaryFromText(text,dictionary):
    words=text.split()
    for word in words:
        if word not in dictionary:
            dictionary[word]=1
        else:
            dictionary[word]+=1
    return dictionary

wood_dictionary={}
wood_dictionary=dictionaryFromText(cleanText(woodchuck),wood_dictionary)

keylist=list(wood_dictionary.keys())
keylist.sort()
for key in keylist:
    print("{},{}".format(key,wood_dictionary[key]))


#Exercise 16.2
#Do the same thing as you did for the previous exercise, but now process the text line by line.
# This is something that you would have to do if you had to process a very long text.

h=open("pc_woodchuck.txt")
wdict={}
while True:
    line=h.readline()
    if line=="":
        break
    else:
        cleanline=cleanText(line)
        wdict=dictionaryFromText(cleanline,wdict)
h.close()

keylist=list(wdict.keys())
keylist.sort()
for key in keylist:
    print("{},{}".format(key,wdict[key]))"""


"""#Exercise 16.3
#Write a program that processes the contents of “pc_woodchuck.txt,” line by line.
#It creates an output file in the current working directory called “pc_woodchuck.tmp,”
#which has the same contents as “pc_woodchuck.txt,” except that all the vowels are removed (case-insensitively).
#At the end, display how many characters you read, and how many characters you wrote.

h=open("pc_woodchuck.txt")
h1=open("pc_woodchuck.tmp","w")

def removeVowels(text):
    lowertext=text.lower()
    novwltxt=""
    for ch in lowertext:
        if ch in "aeiou":
            novwltxt+=""
        else:
            novwltxt+=ch
    return novwltxt

read=0
written=0
while True:
    line=h.readline()
    if line=="":
        break
    else:
        read+=len(line)
        ln=removeVowels(line)
        written+=len(ln)
        h1.write(ln)

h.close()
h1.close()

print("The initial number of character was {}, the number of copied characters is {}.".format(read,written))
"""



"""#Exercise 16.4
#Write a program that determines how many words of 2 or more letters the files “pc_woodchuck.txt,”
#“pc_jabberwocky.txt” and “pc_rose.txt” have in common. You have to treat the words case-insensitively and,
#as always, any character that is not a letter can be treated as a word boundary.
#If your program is correct, you will find three such words.


h1=open("pc_woodchuck.txt")
h2=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_rose.txt")
h3=open("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_jabberwocky.txt")



woodchuck=h1.read()
rose=h2.read()
jabberwocky=h3.read()

def cleanText(text):
    text=text.lower()
    cleantext=""
    for ch in text:
        if ch>="a" and ch<="z":
            cleantext+=ch
        else:
            cleantext+=" "
    return cleantext

def createDictionary(text):
    dict={}
    split_text=text.split()
    for word in split_text:
        if len(word)>=2:
            if word in dict:
                dict[word]+=1
            else:
                dict[word]=1
    return dict

cleanw=cleanText(woodchuck)
wdict=createDictionary(cleanw)

cleanr=cleanText(rose)
rdict=createDictionary(cleanr)

cleanj=cleanText(jabberwocky)
jdict=createDictionary(cleanj)

h1.close()
h2.close()
h3.close()

commonKeys=[]
for key in wdict.keys():
    if (key in rdict.keys()) and (key in jdict.keys()):
        commonKeys.append(key)

print(commonKeys, len(commonKeys))
"""


#For the three files that you used in the previous exercise, count for each of them
# how often each letter (case-insensitively) occurs. Calculate for each letter and
# each file the fraction <number of occurrences of letter in the file>/<total number
# of letters in the file>. Write an outputfile (any name, as long as you can safely overwrite it)
# with extension .csv, that contains 26 lines, each line formatted as follows:
# "<letter>",<fraction for first file>,<fraction for second file>,<fraction for third file>.
# The first line should have letter a, the second letter b, etcetera. The fractions should be
# stored with 5 decimals. Finally, display the contents of the outputfile. As the outputfile is
# a CSV file, you should also be able to load it in a spreadsheet program. A quick check to see
# if you did things correctly is that all of the fractions must be between zero and 1, and the
# fraction for “e” should be highest for both “pc_jabberwocky.txt” and “pc_rose.txt”
# (but not so much for “pc_woodchuck.txt”). If you would use longer files which are all in the
# same language, you would also find that the fractions are usually more or less in each others’ neighborhood.


def letterCounter(filename):
    charDictionary={}
    for i in range(ord("a"),ord("z")+1):
        charDictionary[chr(i)]=0
    with open(filename) as fp:
        for line in fp:
            for ch in line:
                if ch>="a" and ch<="z":
                    charDictionary[ch]+=1
    return charDictionary

def getLetterFrequency(dictionary):
    totChar=sum(dictionary.values())
    newDictionary={}
    for key in dictionary.keys():
        newDictionary[key]=dictionary[key]/totChar
    return newDictionary



def createCSV(list_of_dictionaries): #all dictionaries have the same key
    with open("solution.txt","w") as fp:
        for key in list_of_dictionaries[0].keys():
            fp.write(key)
            for i in range(len(list_of_dictionaries)):
                r5=round(list_of_dictionaries[i][key],5)
                fp.write(","+str(r5))
            fp.write("\n")


d1=letterCounter("pc_woodchuck.txt")
d2=letterCounter("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_rose.txt")
d3=letterCounter("/Users/elvirapapaleo/Documents/MasterBigData/AllPy/pythonbooklistings/pc_jabberwocky.txt")

[d1f,d2f,d3f]=getLetterFrequency(d1),getLetterFrequency(d2),getLetterFrequency(d3)

createCSV([d1f,d2f,d3f])




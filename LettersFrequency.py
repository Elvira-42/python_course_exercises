"""
Create a Frequency class to handle a text file. The class must have (at least) a property called
fileToProcess, whose purpose is to store the text file managed by the class.
– Assume the text file to be processed could be reasonably long (hence, big in size).
– Use .txt as the standard suffix for file names.
"""

class Frequency:
    def __init__(self,FileToProcess,dictionary={}):
        self.FileToProcess = FileToProcess
        self.dictionary = dictionary

    def __repr__(self):
        if not self.dictionary:
            return "text: {}, dictionary: standard alphabet".format(self.FileToProcess)
        else:
            return "text {}, dictionary: {}".format(self.FileToProcess,self.dictionary)

"""
Create a guess6 method that analyzes fileToProcess as follows:
– Reads the file managed by the class (using an appropriate strategy for its length).
– Returns the string composed of the six most frequent characters in fileToProcess, in de-
scending order of frequency, considering the following rules:
∗ Ignore the distinction between uppercase and lowercase letters.
∗ Include accented letters.
∗ Exclude punctuation and other symbols.
∗ Include numbers.
– In case of a tie in frequency, the characters should be sorted lexicographically.
Use the file divinaCommedia.txt as the reference file, which contains The Divine Comedy in plain
text format. The program must work with any text file given as input to the function.
"""
                                       
    
    def guess6(self, dictionaryExtras=[]):
        #if no dictionary is provided, create dictionary of standard alphabetical characters
        if not self.dictionary:
            for i in range(ord("a"), ord('z') + 1):
                self.dictionary[chr(i)] = 0
        #if list with Dec references of extra characters is provided, add them to the dictionary
        for i in dictionaryExtras:
            self.dictionary[chr(i)]=0
        if len(self.dictionary)<6:
            raise IndexError ("The dictionary should have at least 6 entries", len(self.dictionary))
        #populate the dictionary values
        with open (self.FileToProcess) as fp:
            for line in fp:
                line=line.lower()
                for ch in line:
                    if ch in self.dictionary:
                        self.dictionary[ch] = self.dictionary[ch]+1
        #order frequencies high to low
        freq=list(self.dictionary.values())
        freq.sort(reverse=True)
        #create new dictionary with most frequent 6 letters
        f6=''
        for i in range(6):
            ind=list(self.dictionary.values()).index(freq[i])
            key=list(self.dictionary.keys())[ind]
            f6 += key
        return f6



#create list of extra characters, including numbers and italian accented letters
extraChar=[]
for i in range(0,10):
    extraChar.append(ord(str(i)))
dcodes=[224,232,233,236,242,249]
for i in dcodes:
    extraChar.append(i)



YeOldeItalian = Frequency("divinaCommedia.txt")
YeOldeItFrequency = YeOldeItalian.guess6(extraChar)
print("Most frequent letters in old Italian: ", YeOldeItFrequency)

YeOldeEnglish = Frequency("MerryWives.txt")
YeOldeEnFrequency = YeOldeEnglish.guess6()
print("Most frequent letters in old English: ", YeOldeEnFrequency)

ModernEnglish=Frequency("PrideAndPrejudice.txt")
NewEnFrequency = ModernEnglish.guess6()
print("Most frequent letters in modern English: ", NewEnFrequency)


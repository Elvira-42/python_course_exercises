"""#There is also a set method symmetric_difference() which returns a set that contains
# all the elements that are in the union of two sets, except those that are found in both sets.
# For example, if set 1 contains A, B, and C, and set 2 contains B, C, and D,
# the symmetric difference of sets 1 and 2 contains A and D. Can you implement the symmetric_difference()
# method by using only some of the methods found above?

a={"Scotland","Italy","Netherlands","South Korea","Madagascar"}
b={"Mexico","Peru","Madagascar","Scotland"}

def symmDiff(set1,set2):
    u=set1.union(set2)
    i=set1.intersection(set2)
    sd=u.difference(i)
    return sd

print(symmDiff(a,b))"""

"""#In the chapter on iterations you were asked to write code that determines all the letters that
# two words have in common, whereby each letter should only be reported once. Using sets,
# you can do this very efficiently. Please write the appropriate code.

a=set("chameleon")
b=set("walrus")
commonLetters=a.intersection(b)
print(commonLetters)
"""


"""#Exercise14.1
#A famous syllogism says: All men are mortal. Socrates is a man. Therefore Socrates is mortal.
# In the code block below you see some sets. The first is the set of all things (I know a few are missing,
#but for the sake of argument). The second is the set of all men (assuming that the first set indeed contains
# all things). The third set contains everything that is mortal (again, assuming...).
# Using set operators and methods, show that indeed (a) all men are mortal, (b) Socrates is a man,
# and (c) Socrates is mortal. Also shows that (d) there are mortal things that are not men, and
# (e) there are things that are not mortal.

allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera",
    "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates","Plato","Eratosthenes","Cat","Dog"}


#all men are mortals
if men.issubset(mortalthings):
    print("All men are indeed mortal!")

#Socrates is a man
if "Socrates" in men:
    print("Socrates was found amongst the men")

#Socrates is mortal
if "Socrates" in mortalthings:
    print("Socrates is also mortal")

#some mortal things are not men
diff=mortalthings.difference(men)
if len(diff) > 0:
    print("Some mortal things, like {}, are not men".format(diff))

#there are things that are not mortal
immortal=allthings.difference(mortalthings)
if len(immortal) > 0:
    print("There are things that are not mortal")"""



#Exercise 14.2
#Write a program that first produces three sets of numbers between 1 and 1000, the first
#all those numbers that are divisible by 3, the second all those numbers that are divisible by 7,
#and the third all those numbers that are divisible by 11. It is easiest to do that with list
#comprehension, but it is not necessary. Now produce sets of all the numbers between 1 and1000 that
#(a) are divisible by 3, 7, and 11, (b) are divisible by 3 and 7, but not by 11,
#(c) that are not divisible by 3, 7, or 11. The shortest solution has only one line of code for each of the six sets.
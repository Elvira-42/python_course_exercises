"""#The code below can generate several exceptions. These are now handled by a single try ... except clause.
#Extend this code by handling all exceptions that may occur explicitly (there are at least three
# different kinds of exceptions that can be raised).

fruitlist = ["apple", "banana", "cherry"]
try:
    num = input( "Please enter a number: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except ValueError:
    print("You have not entered a number")
except TypeError:
    print("Only integers are supported for indexing")
except IndexError:
    print("The element you are trying to access does not exist")
except:
    print( "Something went wrong" )"""


#Exercise 17.1
#Which exceptions can the code below raise? Extend the code to handle all of them in a reasonable manner.


numlist = [ 100, 101, 0, "103", 104 ]
try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except IndexError:
    print("Your index is out of bounds")
except ValueError:
    print("You have not entered an integer")
except TypeError:
    print("You cannot divide an integer by a string")
except ZeroDivisionError:
    print("Dividing by zero is not allowed")
#Poet and the Pendelum solution
#Inspired by a codewars problem
#This program will take a set of inputs from a user and sort them from lowest to highest
#After that it will place the lowest number in the center of the list, the second highest next to it, the next highest to the right of that, etc.
#Example is a set of number [1,4,15,2,9,7,5,4] would be sorted to [1,2,4,4,5,7,9,15] then [9,5,4,1,2,4,7,15]

x = 0
y = 0
userInput = [ ]

while True:
    try:
        inp = int(input("Insert some numbers(Type -1 to finish): "))
    except ValueError:
        inp = int(input ("Numbers only please: "))
    if inp >= 0:
        userInput.append(inp)
    if inp == -1:
        break
       
        
print("Your numbers are ")
arrayLength = len(userInput)
#arrayLength -= 1
x = 0
print (" ".join(map(str,userInput)))
userInput.sort()
print("in order these numbers are: ")
print (" ".join(map(str,userInput)))
newList = [ ]

for x in range(0, arrayLength):
    if (x % 2) == 0:
        newList.append(userInput[x])
    if (x % 2) == 1:
        newList.insert(0, userInput[x])


print("as a pendelum these numbers form: ")
print(" ".join(map(str,newList)))

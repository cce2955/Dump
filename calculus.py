#-------------------------------
#---------------------------------

#Let Phi of X equals Pi Product Notation (rangin from 1 to infinity
#(which will be changed at my discretion D:) while  (1 - x superscript n)
#
#-----------------------------------
#----------------------------------

import math

#print (math.pi)

#creates a makeshift equation of pi since I can't find the proper library for it, phisolved is the
#output, phicomponent is the input, repalce with X as applicable

def phi ():
    global phiSolved 
    phiSolved = math.pow(phiComponent, 2) - phiComponent - 1
    
   # print (phiSolved)
    
   #don't print this unless testing again



#creates a product summation of 1-x^2, n Range determines the range and the first value follows
#N's starting point
#this does not function with the full equation only works as its own module, do not call when main
#equation is formed
#sumStart and sumFinish is implied to utilize input from user if this project goes that far, for now 
#it'll have preinput values before I get to that point
#because of the huge range of numbers this processes it will more than like start an error
#so attempting to go to a range of infinity is literally not possible no matter how I optomize 
#this code
#However if I care hard enough I'll look into creating a custom counting system
#--------------------------------------
#try not to go over 50
sumStart = 1
sumFinish = 49
#-----------------------------------------

 
productSum2 = 1

for n in range (sumStart,sumFinish):
    phiComponent = n
    phi()
    productSum = 1 - math.pow(phiSolved , n)
    productSum2 = productSum * productSum2
    print ("initial Product sum ", productSum)
    print ("Totient ",  phiSolved)
    print ("Total Product Sum ", productSum2)

#This is as far as I go, running this program causes the total product sum to go to zero since after 3 steps the sum reaches zero
#and forces the product to stay stuck at zero
#I could fix this easily but that's disrespectful to the math....assuming I even did this correctly
#I will invest in a notebook and do the calculations myself and see if I can figure out what's going on, for now this will be posted
#to my github as an attempt

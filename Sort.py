import json
import sys
import os


#makes sure the propper arguments are inputed
if len(sys.argv) != 2:
	print('Error: Invalid Input')
	sys.exit(1)

try:
	sortedList = []
        
	#opens a given file
        with open(sys.argv[1], "r") as file:
        	data = file.readlines()
            
            
		#Sort into list here
        	for line in data:
                

		
	file.close()
                    
		
	
	#prints out the sorted list of words
        for x in sortedList:
		print(x)     
            

        
        
         
       
        



#In case the given file isn't there
except FileNotFoundError:
	print('ERROR: File Not Found')
	exit(1)

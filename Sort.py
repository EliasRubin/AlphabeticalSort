import json
import sys
import os
from scipy.io import arff


if len(sys.argv) != 2:
    print('Error: Invalid File')
    sys.exit(1)

try:
	sortedList = []
        
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            
            
            for line in data:
                #Sort into list here

	file.close()
                    
		
		
        for x in sortedList:
  		print(x)     
            

        
        
         
       
        




except FileNotFoundError:
            print('ERROR: File Not Found')
            exit(1)

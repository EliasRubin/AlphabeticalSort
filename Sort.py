import json
import sys
import os
from scipy.io import arff


if len(sys.argv) != 2:
    print('Error: Invalid File')
    sys.exit(1)

try:
        
        with open(sys.argv[1], "r") as file:
            data = file.readlines()
            name,ext = os.path.splitext(file.name)
            
            csvSwitch = False
            header = ""
            newCsv = []

            
            for line in data:
                #Sort into list here

	    file.close()
                    
            #recursively print the list
            
            

        
        
         
       
        




except FileNotFoundError:
            print('ERROR: File Not Found')
            exit(1)
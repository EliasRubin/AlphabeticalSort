import json
import sys
import os

# n is size of heap 
def heapify(list, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and list[i] < list[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and list[largest] < list[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        list[i],list[largest] = list[largest],list[i]  # swap 
  
        # Heapify the root. 
        heapify(list, n, largest) 
  
# The main function to sort an array of given size 
def sort(list): 
    n = len(list) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(list, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        list[i], list[0] = list[0], list[i]   # swap 
        heapify(list, i, 0) 
	
	
	
#makes sure the propper arguments are inputed
if len(sys.argv) != 2:
	print('Error: Invalid Input')
	sys.exit(1)

try:
	
        
	#opens a given file
        with open(sys.argv[1], "r") as file:
        	list = file.readlines()
            	
		
		
		#Sort into sortedList here
		
		
		
		sort(list)
		
		
		
        	for line in data:
			#This section inserts the first two values into the list to work with
        		
			
           	
                

		file.close()
                    
		
		#prints out the sorted list of words
        	for x in listist:
			print(x)     
            

        
        
         
       
        



#In case the given file isn't there
except FileNotFoundError:
	print('ERROR: File Not Found')
	exit(1)

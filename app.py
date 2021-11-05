def matchingSocks(socks):
    #Creating a dictionary object to help us calculate the frequency of each color.
    pairsofsocks = {}
    
    #Looping through the list of socks to categorize the colors into their frequencies.
    for sock in socks:
        if sock not in pairsofsocks:
            #Add to the dictionary if color does not already exist in the dictionary 
            pairsofsocks[sock] = 1
        else:
            #If color already exists in dictionary add one to it.
            pairsofsocks[sock] += 1
            
    #Initializing a variable to store the total number of pairs
    pairs = 0
    #Looping through the colors in the dictionary
    for pair in pairsofsocks:
        #We divide the value of the color by two in order to
        #get the number of pairs of that color.
        pairs += pairsofsocks[pair] // 2
        
    if pairs == 0:
        return "The total number of pairs in this pile is " + str(pairs) + "."
    else:
        return "The total number of pairs in this pile is 0."
    
#Initializing the first test which contains 30 elements and 10 pairs
socks1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,10]
#Printing the number of socks in the array
print(len(socks1))
#Printing the result of our function which is the number of matching socks.
print(matchingSocks(socks1))

#Initializing the second test which contains 80 elements and 36 pairs
socks2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,50,51,52,53,54,55,56,57]
#Printing the number of socks in the array
print(len(socks2))
#Printing the result of our function which is the number of matching socks.
print(matchingSocks(socks2))

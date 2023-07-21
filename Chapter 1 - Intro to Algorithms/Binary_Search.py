def binary_search(list, item):
    low = 0  #keep track of the lowest number
    high = len(list) - 1  #keep track of the highest number
    
    while low <= high: #run the while loop until the lowest number is less than or equal to the highest number
        
        mid = (low + high) // 2 #find the middle of the list 
        if item == list[mid]: #if the item to be founded is the same as the value of the middle in list -> return the item
            return mid
        
        elif item > list[mid]: #if the item is bigger than the value -> increase the lowest value by adding 1 to the middle value
            low = mid + 1
            
        else: #else if the value is less than the higher value, decrease the highest value by subtracting the mid value by 1
            high = mid - 1
            
    return None #if item is not found -> return 'None'

list = [1, 3, 5, 7, 9]
print(binary_search(list, 5))   
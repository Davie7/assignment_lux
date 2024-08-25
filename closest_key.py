# The following function takes a dictionary with keys as letters and values as lists of letters, 
# It then proceeds to find the key with the input value closest to the beginning of the list:

def closest_key(dictionary, target_value):
    min_index = float('inf')
    closest_key = None
    
    for key, value_list in dictionary.items():
        if target_value in value_list:
            current_index = value_list.index(target_value)
            if current_index < min_index:
                min_index = current_index
                closest_key = key
    
    return closest_key

# Testing the function
test_dict = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['C', 'D', 'A', 'E'],
    'C': ['D', 'E', 'A', 'B'],
    'D': ['A', 'B', 'C', 'E']
}

print(closest_key(test_dict, 'E'))  
print(closest_key(test_dict, 'A'))  
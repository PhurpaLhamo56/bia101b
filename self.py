
input_str = "((()"

floor_index = 0 # variable to keep track of the ans
for i in input_str: # go through each character 
    if i == "(": # if ( add one to the answer
        floor_index = floor_index += 1
    if i == ")": # if sub one to the answer 
        floor_index floor_index -= 1

# print the final answer
print('the final floor is', floor_index) 


# searching
# sorting

# !problem 1

# input
user_input = [1,2,3,4,5,6,7,8,9,11]


# ?Q: Check to see if a certain number exist in the user input array
n = 3


# linear search
result = False # variable to keep track of your answer
for e in user_input:
    if e == n:
        result = True

if result == True:
        print('exist')
else: 
        print('Not exist')
# if else, for loops, print, calculation(+. -)

# Time: O(n)
input = [1,2,3,4,5,]
for i in input:
    if i == 1: #O(1)
        continue
    print('hi')

input = [1,2,3,1,1,1]
#O(n^2)
for i in input:
     print('hey')
for k in input:
     print('hello')




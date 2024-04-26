input_str = "((((()))))"

stack = []

for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
         stack.pop()
length = len(stack)
if length == 0:
    print('True')
else:
    print('False')       
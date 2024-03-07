#. objectives: calculator.application.made.using.
#.variables.and.if. statements

# steps
# 1. get input from user
# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 
# 3. give output to the user

print('* for multiplication')
print('+ for addition')
print('- for subtration')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

if whatUserTyped == "+":
    print('Doing Additon')
    print('doing more addtion')

    if whatUserTyped == "-":
        print('Doing substration')
        print('doing more substration')

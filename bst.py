rpn = []
userInput = 0

'''

while (type(userInput) == int):    #while the input is of int
    userInput = input()            #set the input to a name
    rpn.append(int(userInput))     #add the userInput to the end of rpn list
    if (type(userInput) == "+"):   #if userInput is of type "+"
        var1 = rpn.pop()           #pop var1 from end of the list
        var2 = rpn.pop()           #pop var2 from end of the list
        rpn.append(var1+var2)      #add the result of 'var1+var2' to end of list
        print(int(var1+var2)       #print result from ^

'''


truth = 1
stack = list()
while(truth == 1):
    currentInput = input()
    if (currentInput.isnumeric == True):
        Stack.append(int(currentInput))
        print(int(currentInput))
    elif (currentInput == "+"):
        num1 = Stack.pop()
        num2 = Stack.pop()
        Stack.append(num1 + num2)
        print(int(num1 + num2)

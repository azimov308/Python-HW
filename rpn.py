rpn = []
userInput = 0
cont = 1

while(cont == 1):
    userInput = raw_input()
    try:
        userInput = int(userInput)
        rpn.append(userInput)
    except ValueError:
        if not rpn:
            print("invalid operation1")
        elif (len(rpn) > 1 and userInput == "+"):
            var1 = rpn.pop()
            var2 = rpn.pop()
            rpn.append(var1+var2)
            print(var1+var2)
        elif (len(rpn) > 1 and userInput == "-"):
            var1 = rpn.pop()
            var2 = rpn.pop()
            rpn.append(var2-var1)
            print(var2-var1)
        elif (len(rpn) > 1 and userInput == "*"):
            var1 = rpn.pop()
            var2 = rpn.pop()
            rpn.append(var1*var2)
            print(var1*var2)
        elif (len(rpn) > 1 and userInput == "/"):
            var1 = rpn.pop()
            var2 = rpn.pop()
            rpn.append(var1/var2)
            print(var1/var2)
            #print(float(var1/var2)) <--don't know abt this one
        elif (userInput == "~"):
            var1 = rpn.pop()
            rpn.append(var1*-1)
            print(var1*-1)
        elif (type(userInput) != int):
            print("invalid operation2")

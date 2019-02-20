rpn = []
userInput = 0
con = 1

while(con == 1):
  userInput = raw_input()
  try:
    userInput = int(userInput)
    rpn.append(userInput)
  except ValueError:
    if not rpn:
        print("invalid")
    elif (len(rpn)>1 and userInput== "+"):
        var1 = rpn.pop()
        var2 = rpn.pop()
        rpn.append(var1+var2)
        print(int(var1+var2))
    elif (len(rpn)>1 and userInput == "-"):
        var1 = rpn.pop()
        var2 = rpn.pop()
        rpn.append(var2-var1)
        print(int(var2-var1))
    elif (len(rpn)>1 and userInput == "*"):
        var1 = rpn.pop()
        var2 = rpn.pop()
        rpn.append(var1*var2)
        print(int(var1*var2))
    elif (len(rpn)>1 and userInput == "/"):
        var1 = rpn.pop()
        var2 = rpn.pop()
        rpn.append(var1/var2)
        print(int(var1/var2))
    elif (userInput == "~"):
        var1 = rpn.pop()
        rpn.append(var1*-1)
        print(int(var1*-1))
    elif (type(userInput) != int):
            print("invalid")

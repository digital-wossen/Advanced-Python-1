# JTSK-350112
# a1 5.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



stack = [28,55,77,111,7,2,14,5,7, 8,3,7, 4, 11]
print("Stack: {}".format(stack))
while True:
    
    l = input()
    if l == 's':
        n = input()
        stack.append(n)# maintain count of popped elements 
        print("Pushing {:}".format(n))
    elif  l == 'p':
        if len(stack) > 0:
            stack.pop(1)
            print("Popping element {:}".format(stack.pop()))
        else:
            print("Stack Underflow")
    elif l == 'e':
        stack.clear()
        print("Emptying Stack")
    elif l == 'q':
        print("Good Bye!")
        break


    

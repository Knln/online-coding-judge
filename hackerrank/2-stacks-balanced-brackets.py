def is_matched(expression):
    stack = []
    
    for exp in expression:
        if (exp == '{'):
            stack.append(exp)
        elif (exp == '['):
            stack.append(exp)
        elif (exp == '('):
            stack.append(exp)
        elif (exp == ')'):
            if not stack:
                return False
            if(stack[len(stack)-1] == '('):
                stack.pop()
            else:
                return False
        elif (exp == ']'):
            if not stack:
                return False
            if(stack[len(stack)-1] == '['):
                stack.pop()
            else:
                return False  
        elif (exp == '}'):
            if not stack:
                return False
            if(stack[len(stack)-1] == '{'):
                stack.pop()
            else:
                return False  
    if stack:
        return False
    else: 
        return True

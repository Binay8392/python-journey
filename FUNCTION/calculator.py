def calculator(a,b,op):
    if op =='+':
        return a+b
    elif op =='-':
        return a-b
    elif op =='*':
        return a*b
    elif op =='/':
        return a/b  
    else:
        return "Invalid operator"



a =int(input('enter 1st number : '))     
b =int(input('enter 2nd number : '))     
op =input('enter operator : ')     

print(calculator(a,b,op))   
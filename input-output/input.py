print ('enter 1st number :')
num1 = input() #input function takes input from user and returns it as a string
print ('enter 2nd number :')
num2 = input()
print ('the sum of two numbers is : ' + str(int(num1) + int(num2))) #we have to convert the input to integer before adding them, because input function returns a string. We can also use float() function if we want to take decimal numbers as input.


print(bool("")) #empty string is considered as False
print(bool("hello")) #non-empty string is considered as True
print(bool(0)) #zero is considered as False
print(bool( )) #empty space is considered as False
print(bool(-1)) #non-zero is considered as True         
print("Hi, what you gonna do today?")
print('1 - sum\n2 - subtraction\n3 - multiplication\n4 - division')
q = int(input('your choice '))
if q == 1:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a + b)

elif q == 2:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a - b)

elif q == 3:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a * b)

elif q == 4:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a / b)
    
else:
    print('wrong operation')

# ЫЫЫЫ
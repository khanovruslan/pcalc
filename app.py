print("Hi, what you gonna do today?")
print('1 - sum\n2 - subtraction')
q = int(input('your choice '))
if q == 1:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a + b)

elif q == 2:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print('result', a - b)

else:
    print('wrong operation')
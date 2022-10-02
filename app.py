print("Hi, what you gonna do today?")
print('1 - sum')
q = int(input('your choice '))
if q == 1:
    a = int(input('first number please '))
    b = int(input('second number please '))
    print(a + b)
else:
    print('wrong operation')
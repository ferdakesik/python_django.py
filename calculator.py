
num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
op=input('enter operator: ')

if op == '+':
    print('the addition is ' , num1+num2)
elif op=='-':
    print('the substrution is ', num1-num2)
elif op=='*':
    print('the multiplication is ', num1*num2)
elif op=='/':
    print('the division is ', abs(num1/num2))
else:
    print('invalid operator')
    

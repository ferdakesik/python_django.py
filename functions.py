
def greetings_function():
    print("new message")

greetings_function()

def greetings(name):
    print('welcome',name)
greetings('ferda')

def sayi(*name):
    print('welcome'+name[1])
sayi('ferda','lal','marti')

def olmak(name, age):
    print('welcome'+name+'. you are '+str(age)+' years old.')

name= input('enter your name: ')
age= input('enter your age: ')
olmak(name,age)




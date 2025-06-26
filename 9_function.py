
def greet():
    """Display a hi message to user"""
    print("Hello world")

greet()



def greet(name):
    """Display a hi message to user"""
    print("hi",f"my name is {name} ")

greet("omkar")



# Position arguments
def greet(name,city):
    """Display a hi message to user"""
    print("hi",f"my name is {name} and i am from {city}")

greet("omkar","Kallam")


# defualt arguments
def greet(name="omkar",city="kalla"):
    """Display a hi message to user"""
    print("hi",f"my name is {name} and i am from {city}")

greet(name="omkar")



# # return statement

def add_numbers(x, y):
    """Function to add two numbers."""
    return x + y

output=add_numbers(10,20)
print(output)


def add(num1,num2):
    sum=num1+num2
    print(sum)
add(10,20)

def add(num1,num2):
    sum=num1-num2
    print(sum)
add(num2=10,num1=20)


def add(num1,num2):
    sum=num1*num2
    print(sum)
add(num2=10,num1=20)


def add(num1,num2):
    sum=num1/num2
    print(sum)
add(num2=10,num1=20)


def add(num1,num2):
    sum=num1**num2
    print(sum)
add(num2=10,num1=20)




def output(num):
    for i in range(1,11):
        print(i*num)

output(int(input("Enter a number : ")))



def get(num1,num2):
    sum=num1+num2
    print(sum)


a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
get(a,b)







def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

read = input("Enter choice: ")
num1 = float(input("Enter first num: "))
num2 = float(input("Enter second num: "))

if(read == '1'):
    print("its one Answer is",add(num1,num2))
elif(read == '2'):
    print("its two",sub(num1,num2))
elif(read == '3'):
    print("its three",mul(num1,num2))
elif(read == '4'):
    print("its four",div(num1,num2))


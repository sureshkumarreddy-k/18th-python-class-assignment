1. write a program to print the grade of a student based on the marks obtained. 
2. Write a program to print if the guven year is leap or not.
3. Write a program to print if the given number is zero or odd or even.
4. Write a program to check the strength of a password.(please provide different rules for the password)
5.Write a program to create a calculator that perform basic arithematic operations.
1.
marks=int(input("Enter marks:"))
if(marks>=90):
    print("Grade A")
elif (marks>=80 and marks<90):
    print("Grade B")
elif (marks>=70 and marks<80):
    print("Grade C")
elif (marks>=60 and marks<70):
    print("Grade D")
elif (marks>=50 and marks<60):
    print("Grade E")
elif (marks>=40 and marks<50):
    print("Grade E")
else:
    print("Fail")
    
2.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
 
3.
num=int(input("Enter a number"))
if(num==0):
    print("zero")
elif(num%2==0):
    print(num,"is Even")
else:
    print(num,"is odd")
    
4.
def check_password(password):
    length = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    specialchar = any(c in "!@#$%^&*()" for c in password)

    if (length and uppercase and lowercase and digit and specialchar):
        print("Strong Password")
    elif length and digit and specialchar:
        print("Moderate Password")
    else:
        print("Weak Password")
password=input("Enter password: ")
check_password(password)
    
5.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /,%): ")
if op == "+":
    print("Addition is",num1+num2)
elif op == "-":
    print("Subtraction is",num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 == 0:
        print("Error: division by zero.")
    else:
        print("Division is",num1/num2)
elif op == "%":
    if num2 == 0:
        print("Error: division by zero.")
    else:
        print("Division is",num1%num2)
else:
    print("Error: invalid operator.")


# Program make complexcalculator CLI
# This function adds twenty six numbers
def add(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z):
    return a+ + b + c + d + e + f + g + i + j + k + l + m + n + o + q + r + s + t + u + v + w + x + y + z

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

# This function finds the remainder of 2 numbers
def divide(x,y):
    return 



print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.find remainder of 2 numbers")
print("6.square of a number")
print("7.square root of a number under construction")
print("8.Cube of a number under construction")
print("9.Lowest common multiple under construction")
print("10.Highest common multiple under construction")
while True:


    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        num5 = float(input("Enter fifth number: "))
        num6 = float(input("Enter sixth number: "))
        num7 = float(input("Enter seventh number: "))
        num8 = float(input("Enter eighth number: "))
        num9 = float(input("Enter ninth number: "))
        num10 = float(input("Enter tenth number: "))
        num11 = float(input("Enter eleventh number: "))
        num12 = float(input("Enter twelfth number: "))
        num13 = float(input("Enter thirteenth number: "))
        num14 = float(input("Enter fourteenth number: "))
        num15 = float(input("Enter fifteenth number: "))
        num16 = float(input("Enter sixteenth number: "))
        num17 = float(input("Enter seventeenth number: "))
        num18 = float(input("Enter eighteenth number: "))
        num19 = float(input("Enter nineteenth number: "))
        num20 = float(input("Enter twentieth number: "))
        num21 = float(input("Enter twenty-first number: "))
        num22 = float(input("Enter twenty-second number: "))
        num23 = float(input("Enter twenty-third number: "))
        num24 = float(input("Enter twenty-fourth number: "))
        num25 = float(input("Enter twenty-fifth number: "))
        num26 = float(input("Enter twenty-sixth number: "))
     
 
        if choice == '1':
            print(num1, "+", num2, "+", num3,"+", num4, "+", num5,"+", num6,"+", num7, "+", num8,"+", num9, "+", num10,"+", num11,"+", num12, "+", num13, "+", num14,"+", num15, "+", num16, "+", num17,"+", num18,"+", num19, "+", num20, "+", num21, "+", num22, "+", num23, "+", num24, "+", num25, "+", num26 "=", add(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16, num17, num18, num19, num20, num21, num22, num23, num24, num25, num26))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        elif choice == '5':
            print(num1,"/", num2, "=", (num1 % num2))
        
        elif choice == '6':
            
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")
print("Welcome to the Pattern Generator and Number Analyzer !\n")
is_on=True
while is_on:
    choice= int(input("\nSelect an option:\n 1. Generate a Pattern\n 2. Analyze a range of numbers\n 3. Exit\n Enter your Choice:"))
    if choice == 1:
        pattern_type=int(input("\nChoose a pattern type\n 1. Right Angled triagle\n 2. pyramid\n 3.Left Angled triagle\n Enter your Choice:"))
        if pattern_type == 1:
            row = int(input("Enter the number of rows :"))
            print("\nPattern:")
        
#RIGHT ANGELD TRIANGLE
        
            for i in range (1,row+1):
                for j in range (1,i+1):
                    print("*",end = '',sep = "  ")
                print()
            
#PYRAMID
            
        elif pattern_type == 2:
            row = int(input("Enter the number of rows :"))
            for i in range(1,row+1):
                for k in range(row,i,-1):
                    print(" ",end="")
                for j in range(1,i+1):
                    print("*  ",end="",sep=" ")
                print()
            
#LEFT ANGLED TRIANGLE
        elif pattern_type == 3:
            row = int(input("Enter the number of rows :"))
            for i in range(1,row+1):
                for k in range(row,i,-1):
                    print(" ",end="")
                for j in range(1,i+1):
                    print("*",end="",sep=" ")
                print()
        else:
            print("you have entered a wrong input:")

# ANALYZE A RANGE NUMBER

    elif choice == 2:
            a = int(input("Enter the start of the range: "))
            b = int(input("Enter the end of the range: "))
            print("\n")
            total=0
            for i in range(a,b+1):
                if i%2 == 0:
                    print(i,"NUMBER IS EVEN")
                else:
                    print(i,"NUMBER IS ODD")
                total = total + i
            print("sum of all numbers:",total)

#EXIT
    elif choice == 3:
        print("\nExiting the program. Goodbye! ")
        is_on=False
    else:
        print("\nYOU HAVE ENTERED A WRONG INPUT:  ")
        is_on=False
    
        
        

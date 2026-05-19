print("hello sir, i give a many option to you to choose from you select one of them")

while True:
    print("1.Genrate a patten")
    print("2.Analyze a Range of numbers")
    print("3.Exit the program")

    choice=int(input("Enter your choice:"))
    if choice ==1:
        print("enter your row numbers")
        row=int(input())
        for i in range(row):
            for j in range(i+1):
                print("*",end=" ")
                i=i+1
            print()

    elif choice==2:
        # choice=int(input())    
        first=int(input("Enter starting numbers:"))
        last=int(input("Enter ending numbers:"))

        sum=0

        for i in range(first,last+1):
            if i%2==0:
                print(i, "is Even")
            else:
                print(i,"is Odd")

                sum = sum + i
        total=sum
        print("\nTotal sum=",total)

    elif choice==3:
        print("thank you for using this program")
        print("program closed successfully")
        break

    else:
        print("invaild option try again")


    
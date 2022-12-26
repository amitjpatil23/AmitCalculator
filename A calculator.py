first = input("enter first number : ")
user = input("enter user (+,-,*,/,%) : ")
second = input("enter second number : ")

if user =="+":
    print(int(int (first)+ int (second)))
elif user =="-":
    print(int(int (first)- int (second)))
elif user =="/":
    print(int(int (first)/ int(second)))
elif user =="%":
    print(int(int (first)* int(second)))
elif user =="*":
    print(int(int(first)* int(second)))

else:
    print("sorry error")
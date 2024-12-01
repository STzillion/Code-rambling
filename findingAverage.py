print("Do you want to caclulate average? yes or no")
userResponse = (input())

if userResponse == "yes":
    number_list = []
    n = int(input("Enter the list size "))
    print("\n")
    for i in range(0, n):
        print("Enter your number", )
        item = int(input())
        number_list.append(item)
        print("User list is ", number_list)
else:
    print("goodbye")

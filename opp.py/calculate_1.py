# created the calculate for shop bill 
sum = 0
while(True):
    user_input = input("Enter the item price or press q to quit:\n")
    if (user_input!='q'):
        sum = sum + int(user_input)
        print(f"Your oder total so far:{sum}")

    else:
        print(f"Your bill total is {sum}. Thanks for shopping with us")
        break
       


 
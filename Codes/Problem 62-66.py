import random
choices = [1, 2, 3]
refrencelist = ['Rock', 'Paper', 'Scissor']
print("\n---------Press C to continue, Press Q to quit----\n")
trigger = input()
while trigger != 'q' and trigger != 'Q':
    choice = input("Please one choice \n1. Rock\n2. Paper\n3. Scissor"
                   "\n\n")
    radomvalue = random.choice(choices)
    print("Computer chose ", refrencelist[radomvalue])
    if choice == radomvalue:
        print("Match tied")
    elif choice == 1 and radomvalue == 2:
        print("You Lost")
    elif choice == 1 and radomvalue == 3:
        print("You won")
    elif choice == 2 and radomvalue == 1:
        print("You won")
    elif choice == 2 and radomvalue == 3:
        print("You Lost")
    elif choice == 3 and radomvalue == 1:
        print("You Lost")
    else:
        print("You won")
    print("\n\n-----Press any key to continue------")
    trigger = input()
name = input("Type your name ")
print("Welcome ", name, " to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?\n ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type to walk around and swim to swim across:\n ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died dehydrated")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?:\n ").lower()

    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you want to talk to him (yes/no)? ").lower()

        if answer == "yes":
            print("You talk to the stranger and he gave you gold. You WIN!")

        elif answer == "no":
            print("You ignored the stranger and he felt offended and you lose.")

        else:
            print("Not a valid option. YOu lose.")

    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")
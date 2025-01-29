print("Welcome to Treasure Island")

choice1 = input("Please Enter which side you want to go Left or Right: ").lower()

if choice1 == "left":
    choice2 = input("Please Say would you like to swim or you need to wait: ").lower()
    if choice2 == "wait":
        choice3 = input("Please enter which door you want to open red or yellow or blue: ").lower()
        if choice3 == "blue":
            print("Game over! You have chosen the door that have gate to the ocean.")
        elif choice3 =="red":
            print("Game Over! You have chosen the door to hell:^:")
        elif choice3 == "yellow":
            print("You have won The Game. You have chosen the door to which have full of treasure and way to (:HEAVEN:)")
        else:
            print("Invalid Input. Sorry try again.")
    else:
        print("you have failed. You are Dead.")
else:
    print("You are a looser. You are Dead.")
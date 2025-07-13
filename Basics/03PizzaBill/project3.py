print("WELCOME TO ISLAND!!!")

disc1 = input("YOU ARE ON THE ISLAND ROAD\nWHERE YOU WISH TO TURN\n\t\"left\" or \"right\" ?\n").lower()

if (disc1 == "left"):
    print("THERE IS A LAKE IN FRONT OF YOU.\n TO REACH THE FINAL DESTINATION YOU HAVE TO CROSS IT.THERE IS NO IMMIDIATE BOAT, SO TO ACCESS A BOAT YOU HAVE TO WAIT A WHILE WHERE YOU'RE NOW.\n WHAT YOU WISH TO DO NOW?")
    disc2 = input("\t\"wait\" or \"swim\"?\n").lower()
    if (disc2 == "wait"):
        print("YOU HAVE REACHED TO THE DESTINATION LAND.\n THERE YOU HAVE THREE DOORS IN FRONT OF YOU.WHICH ONE WILL YOU CHOOSE?")
        disc3 = input("\"red\" or \"blue\" or \"yellow\"\n").lower()
        if (disc3 =="yellow"):
            print("BURNT BY FIRE!!!\n\t**GAME OVER**")
        elif (disc3 == "red"):
            print("EATEN BY BEASTS!!!\n\t**GAME OVER**")
        elif (disc3 == "blue"):
            print("CONGRATS!!! YOU GOT THE TREASURE")
        else:
            print("**GAME OVER!!!**")
    else:
        print("EATEN BY CROCODILE!!!\n\t**GAME OVER**")
   
else:
    print("FAll INTO A HOLE!!!\n\t**GAME OVER**")



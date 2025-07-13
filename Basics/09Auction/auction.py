print("WELCOME TO SILENT AUCTION PLATFORM !!!")

store_datas={}

def check_data():
    msg = "yes"
    while msg == "yes":
        name= input("What's Your Name?: ").capitalize()
        bid= int(input("You Want To Bid?: "))
        store_datas[name]=bid
        msg= input("Anyone Left?: \n if yes type 'yes' otherwise type 'no': ")
        print('\n' * 100)

check_data()

finish = False
while not finish:
    win=0
    winner= ""
    is_draw = False
    draw = []
    for name in store_datas:
        if win < store_datas[name]:
            win= store_datas[name]
            winner= name
        elif win == store_datas[name]:
            is_draw= True
            draw.append(name)

    if is_draw:
        store_datas={}
        draw_between = ""
        for any in draw:
            draw_between += f"{any} , "
        draw_between += f"and {winner}"
        draw.append(winner)

        print(f"Its Draw Between {draw_between}")
        print(f"The Auction Window Will Reopen Only For Them. No Other Can Participate.")
        
        for name in draw:
            print(f"{name}, It's Your Turn!")
            bid= int(input("You Want To Bid?: "))
            store_datas[name]=bid
            print('\n' * 100)
    else:
        finish = True
    

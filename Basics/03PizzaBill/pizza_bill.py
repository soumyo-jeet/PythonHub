bill=0

order=input("You wish to order pizza of size: \"big\" , \"small\" or \"medium\"\t").lower()
pepponai=input("Do you wish extra pepponai on your pizza?: 'Y' or 'N'\t").lower()
cheese=input("Do you wish extra cheese on your pizza?: 'Y' or 'N'\t").lower()

if order=="big":
    bill+=200
    if pepponai=="y":
        bill+=3
elif order=="medium":
    bill+=150
    if pepponai=="y":
        bill+=3
elif order=="small":
    bill+=100
    if pepponai=="y":
        bill+=2
else:
    print("Sorry! you typed wrong!!!")




if cheese=="y":
    if order=="big" | order=="small" | order=="medium":
        bill+=5

    


print(f"You final bill is: ${bill}")
letter = ['A','B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]



def your_word():
    word= input("Entre A Word: ").upper()
    print(word)
    shift= int(input("How Much Shift You Want: "))
    dis= input("For encoding type 'encode' Otherwise type 'decode' for decoding: ").lower()

    if dis == 'decode':
        shift *= -1

    display=''
    for each in word:

        if each in letter:
            index = letter.index(each)

            new_index= (index + shift) % len(letter)

            display += letter[new_index]
        else:
            display += each

        
    print(f"You {dis}ed word is" , display)

msg= "yes"
while msg == "yes":
    your_word()
    msg = input("Do You Want To Retry?: \n\t Type 'yes' or 'no' : ").lower()









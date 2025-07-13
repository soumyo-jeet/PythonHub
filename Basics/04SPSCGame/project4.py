import random

choice = ["sc" , "p" , "s"]

art_of_choice= [
    '''
        ()
     (\ ||
      \\||
     /\(\L
     \/ > )
      \( (
       \  \_
      ((\  )\
       \\_/  \
        \_____\ 
    ''',
    '''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
    ''',
    '''

      / )                     
    _( (_    _           
   (((\ \>  /_>         
    ''']


comp_choice = random.choice(choice)
my_choice= input("ENTRE YOUR CHOICE: \n\t 's' for stone or 'p' for paper or 'sc' for scissor").lower()

if my_choice=="s":
    print(f"You choose:{art_of_choice[2]}")
    if comp_choice=="s":
        print(f"Computer choose:{art_of_choice[2]}")
        print("it's Draw!!!")
    elif comp_choice=="sc":
        print(f"Computer choose:{art_of_choice[0]}")
        print("You won!!!")
    else:
        print(f"Computer choose:{art_of_choice[1]}")
        print("You Loose!!!")
    

elif my_choice=="p":
    print(f"You choose:{art_of_choice[1]}")
    if comp_choice=="p":
        print(f"Computer choose:{art_of_choice[1]}")
        print("it's Draw!!!")
    elif comp_choice=="s":
        print(f"Computer choose:{art_of_choice[2]}")
        print("You won!!!")
    else:
        print(f"Computer choose:{art_of_choice[0]}")
        print("You Loose!!!")


elif my_choice=="sc":
    print(f"You choose:{art_of_choice[0]}")
    if comp_choice=="sc":
        print(f"Computer choose:{art_of_choice[0]}")
        print("it's Draw!!!")
    elif comp_choice=="p":
        print(f"Computer choose:{art_of_choice[1]}")
        print("You won!!!")
    else:
        print(f"Computer choose:{art_of_choice[2]}")
        print("You Loose!!!")
    






